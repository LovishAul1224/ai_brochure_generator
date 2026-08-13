# 📄 AI Brochure Generator

An AI-powered application that analyzes a company's website and generates a professional company brochure using Large Language Models.

## Features

-  Scrapes company websites
-  Extracts relevant internal pages
-  Uses an LLM to identify useful pages
-  Generates a professional brochure
-  Markdown preview
-  Download generated brochure
-  Streamlit web interface
-  Environment-based API configuration

## Architecture

```text
User
 │
 ▼
Streamlit UI
 │
 ▼
BrochureService
 │
 ├── WebsiteScraper
 │      └── Website
 │
 ├── LinkSelector
 │      └── LLM
 │
 └── BrochureGenerator
        └── LLM
 │
 ▼
Generated Markdown