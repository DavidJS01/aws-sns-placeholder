package main

import (
	"context"
	"log"
	"github.com/aws/aws-sdk-go-v2/config"
	"fmt"
)

func main() {
    cfg, err := config.LoadDefaultConfig(context.TODO())
if err != nil {
  log.Fatalf("failed to load configuration, %v", err)
} else {
	fmt.Printf("Successfully configured credentials: %v", cfg)
}

// client := s3.NewFromConfig(cfg)

}
