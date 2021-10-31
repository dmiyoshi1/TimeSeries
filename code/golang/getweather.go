package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"net/http"
	"net/url"
	"os"
	"path/filepath"
	"strings"

	"golang.org/x/net/html"
)

func main() {
	myRawDataDir := "/Users/dennismiyoshi/github/TimeSeries/RawData"
	// use locahost with simply pyserver.py to test the code
	webcrawl := "http://localhost/wetter/weather_data.html"
	// webcrawl := "https://www.bgc-jena.mpg.de/wetter/weather_data.html"
	localdataslice := listLocalData(myRawDataDir)

	crawl(webcrawl, localdataslice, myRawDataDir)

	fmt.Println("Done crawling...  Maybe I'll run next time.  :)")
}

func contains(s []string, str string) bool {
	// search through the slice to see if the string is an element in the slice
	for _, v := range s {
		if v == str {
			// return true if the string is found
			return true
		}
	}
	// return false if the string is not found
	return false
}

func getDownloadUrl(uri string, href string) string {
	u, _ := url.Parse(uri)
	fmt.Println(u.Host)

	// if the first character in href is '/' then this is an absolute path
	// else it's relative
	if strings.HasPrefix(href, "/") {
		u.Path = href
		return u.String()
	} else {
		s := strings.Split(u.Path, "/")
		if len(s) > 1 {
			s = s[:len(s)-1]
		}
		u.Path = strings.Join(s[:], "/") + "/" + href
		return u.String()
	}

}

func getTheFile(href string, uri string, localRawDataDir string) (bool, int) {
	fname := localRawDataDir + "/" + href
	out, err := os.Create(fname)
	if err != nil {
		return false, 0
	}
	defer out.Close()

	resp, err := http.Get(uri)
	if err != nil {
		return false, 0
	}
	defer resp.Body.Close()
	n, err := io.Copy(out, resp.Body)
	if err != nil {
		fmt.Println("Error copying to file")
		return false, 0
	} else {
		return true, int(n)
	}
}

func listLocalData(path string) []string {
	var fname []string
	if _, err := os.Stat(path); err != nil {
		fmt.Printf("Doesn't Exist\nCreating the RawData directory")
		os.MkdirAll(path, 0755)
	}
	if files, err := ioutil.ReadDir(path); err != nil {
		log.Fatal(err)
		return fname
	} else {
		for _, f := range files {
			fileExtension := filepath.Ext(f.Name())
			if fileExtension == ".zip" {
				fname = append(fname, f.Name())
			}
		}
		return fname
	}
}

func getHref(t html.Token) (ok bool, href string) {
	// Iterate over token attributes until we find an "href"
	for _, a := range t.Attr {
		if a.Key == "href" {
			href = a.Val
			ok = true
		}
	}
	// "bare" return will return the variables (ok, href) as
	// defined in the function definition
	return
}

// Extract all 'a' href links from a given webpage
func crawl(uri string, localdataslice []string, localRawDataDir string) {
	resp, err := http.Get(uri)

	if err != nil {
		fmt.Println("ERROR: Failed to crawl:", uri)
		os.Exit(1)
	}

	b := resp.Body
	defer b.Close() // close Body when the function completes

	z := html.NewTokenizer(b)

	for {
		tt := z.Next()

		if tt == html.ErrorToken {
			err := z.Err()
			if err == io.EOF {
				//end of the file, break out of the loop
				break
			}
			// There was an error tokenizing,
			// which likely means the HTML was malformed.
			log.Fatalf("error tokenizing HTML: %v", z.Err())
		}

		if tt == html.StartTagToken {
			t := z.Token()
			// Check if the token is an <a> tag
			if isAnchor := t.Data == "a"; isAnchor {
				// Extract the href value, if there is one
				if ok, href := getHref(t); ok {
					if ((strings.HasPrefix(href, "/mpi_roof_2") || strings.HasPrefix(href, "mpi_roof_2")) &&
						strings.HasSuffix(href, ".zip")) &&
						!contains(localdataslice, href) {
						fmt.Println("Downloading", href)
						success, fsize := getTheFile(href, getDownloadUrl(uri, href), localRawDataDir)
						if success {
							fmt.Printf("Successfully retrieved %s with size %d", href, fsize)
						} else {
							fmt.Println("Something failed", fsize)
						}
					}
				}
			}
		}
	}
}
