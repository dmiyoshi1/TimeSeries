package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
	"strings"
    netUrl "net/url"

	"github.com/anaskhan96/soup"
)

func main() {
	myRawData := "/Users/dennismiyoshi/github/TimeSeries/RawData"
	localDataList := listLocalData(myRawData)
	for i, nm := range localDataList {
		fmt.Println(i, nm)
	}
	// webData, err := GetLatestWebData("http://localhost/wetter/weather_data.html")
	GetLatestWebData("http://localhost/wetter/weather_data.html")
	// if err != nil {
	// 	log.Println(err)
	// }
	// fmt.Println(webData)
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

//func GetLatestWebData(url string) (string, error) {
func GetLatestWebData(url string) {
	var ref []string
    u, errr := netUrl.Parse(url)
    if errr != nil {
        os.Exit(1)
    }
    fmt.Println(u)
	// Get the HTML
	resp, err := soup.Get(url)
	if err != nil {
		os.Exit(1)
	}

	doc := soup.HTMLParse(resp)
	links := doc.FindAll("a")
	for _, link := range links {
		// fmt.Println(link.Text(), "| Link :", link.Attrs()["href"])
		if strings.Contains(link.Attrs()["href"], "mpi_roof") {
			ref = append(ref, link.Attrs()["href"])
		}
	}
	fmt.Println(len(ref))
}
