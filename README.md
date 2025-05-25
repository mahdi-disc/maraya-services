# Maraya Services

**Part of the [Maraya (مرايا)](https://github.com/mahdi-disc/maraya)** project — an open-source Dynamic Risk Profiling (DRP) platform designed to reflect and analyze your organization's digital threat surface.

This repository contains the **automated threat detection services** used within Maraya, written in Python. These services continuously scan both your infrastructure and the broader internet to identify Indicators of Compromise (IoCs) and other security threats.

---

## 🧠 What Is Inside?

This repo provides two main services:

| Service Name              | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| `infrastructure_scanner/` | Scans client-owned IP ranges and domains to identify exposed assets, ports, and misconfigurations. |
| `web_crawler/`            | Crawls the public web, deep web, and dark web to discover leaked credentials, impersonation domains, and other external threats. |

Each service is independent, testable, and designed for integration into the Maraya API layer.

---

## 📁 Folder Structure

```
maraya-services/
├── infrastructure_scanner/ # Service for scanning client infrastructure
│ ├── scanner.py
│ └── ...
├── web_crawler/ # Service for crawling public, deep, and dark web
│ ├── subdomains_finder.py
│ └── ...
├── tests/
│ ├── infrastructure_scanner/
│ │ └── test_scanner.py
│ | └── ...
│ └── web_crawler/
│ └── test_subdomains_finder.py
│ | └── ...
├── requirements.txt
├── README.md
└── .env.example
```
