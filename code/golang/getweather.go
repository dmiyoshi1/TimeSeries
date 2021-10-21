package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
)

func main() {
	mycwd, err := os.Getwd()
	myRawData := mycwd + "/RawData"
	if _, err = os.Stat(myRawData); err != nil {
		fmt.Println("Doesn't Exist")
		fmt.Println("Creating the RawData directory")
		os.MkdirAll(myRawData, 0755)
	}
	if files, err := ioutil.ReadDir(myRawData); err != nil {
		log.Fatal(err)
	} else {
		for _, f := range files {
			fileExtension := filepath.Ext(f.Name())
			fmt.Printf("File %s has extenstion %s\n", f.Name(), fileExtension)
			fmt.Println(f.Name())
		}
	}
}
