package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
)

func main() {
	myRawData := "/Users/dennismiyoshi/github/TimeSeries/RawData"
	localDataList := listLocalData(myRawData)
	for i, nm := range localDataList {
		fmt.Println(i, nm)
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
