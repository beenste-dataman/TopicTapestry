

# TopicTapestry 🧵
A robust tool for analyzing and categorizing large datasets using Latent Dirichlet Allocation (LDA).


![image](https://github.com/beenste-dataman/TopicTapestry/assets/50429213/03385c7d-2248-4fbb-917f-b9dd83212a0a)


## Introduction

TopicTapestry is a one stop bulk file handling shop. It sifts through your file names and leverages LDA to categorize them into distinct topics. Whether you're diving into a fresh dataset or revisiting a previous one, TopicTapestry provides a one-stop solution to analyze and make sense of your data.

## Features
- 🗂️ Sort and gather files by type from your unsorted files. Neatly Pack into one directory.
- 📊 Perform LDA analysis on file names.
- 🗂️ Create a CSV flat file database for easy examination.
- 🚀 Quick file retrieval based on topics of interest.
- 🎨 Visualize topic distributions with an interactive HTML output.

## Getting Started

**Clone the Repository**
   ```bash
   git clone https://github.com/beenste-dataman/TopicTapestry.git
   sudo chmod -R 777 TopicTapestry  
   cd TopicTapestry
```

**Run TopicTapestry**
```
python topic_tapestry.py
```


---

## Usage

- **Sort and Gather Files**

Use the sort option to recursively sort files by filetype from your system. This copies them to a bulk target directory. The LDA script takes only a bulk directory as input, no subdirectories. So, this creates a clean bucket for the LDA script to run on. 
I use this script on massive datasets, and love it. It allows me to bucket unmanageable datasets into neat buckets. Then proceed to topic model them using LDA in steps 2-3. Analyze terabytes like they are putty in your hand. 


- **Perform LDA Analysis**

Upon running runner.py, select the option to perform LDA analysis.
The script will guide you through the process.


- **Query prior Results**

Opt to query an existing CSV file.
Enter the topic words of interest.
Access the relevant files directly through the tool.

---


*Requirements
All required packages are listed in requirements.txt. TopicTapestry will handle the installation for you.*

