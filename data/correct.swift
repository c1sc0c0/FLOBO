#!/usr/bin/swift

import Foundation
import Vision
import AppKit

// Check if the correct number of arguments are provided
guard CommandLine.arguments.count == 2 else {
    print("Usage: extract_text.swift <path_to_png_file>")
    exit(1)
}

// Get the file path from the command line arguments
let filePath = CommandLine.arguments[1]

// Ensure the file exists
guard FileManager.default.fileExists(atPath: filePath) else {
    print("File not found at path: \(filePath)")
    exit(1)
}

// Load the image from the file path
guard let image = NSImage(contentsOfFile: filePath) else {
    print("Failed to load image at path: \(filePath)")
    exit(1)
}

// Convert NSImage to CGImage
guard let cgImage = image.cgImage(forProposedRect: nil, context: nil, hints: nil) else {
    print("Failed to convert NSImage to CGImage")
    exit(1)
}

// Create a request handler
let requestHandler = VNImageRequestHandler(cgImage: cgImage, options: [:])

// Create a text recognition request
let request = VNRecognizeTextRequest { (request, error) in
    if let error = error {
        print("Error recognizing text: \(error.localizedDescription)")
        exit(1)
    }

    // Process the recognized text
    if let observations = request.results as? [VNRecognizedTextObservation] {
        for observation in observations {
            if let topCandidate = observation.topCandidates(1).first {
                print(topCandidate.string)
            }
        }
    } else {
        print("No text found")
    }
}

// Set recognition level
request.recognitionLevel = .accurate

// Perform the text recognition request
do {
    try requestHandler.perform([request])
} catch {
    print("Failed to perform text recognition request: \(error.localizedDescription)")
    exit(1)
}