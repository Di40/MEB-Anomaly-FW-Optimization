# Minimum Enclosing Ball for Anomaly Detection using variants of Frank-Wolfe

## Table of contents
* [General Info](#general-info)
* [Group Members](#group-members)
* [Project Structure](#project-structure)
* [Setup](#setup)
* [Usage](#usage)
* [Contributing](#contributing)

## General Info
This is the final project for the "Optimization for Data Science" course at the University of Padova.\
This repository contains the code, [report](./documents/Report%and%Presentation/Report.pdf), [presentation](./documents/Report%and%Presentation/Presentation.pdf) and some [extra materials](https://github.com/Di40/MEB_FrankWolfe_Optimization/tree/main/documents).

### Task
1. Analyze in-depth [four papers](https://github.com/Di40/MEB_FrankWolfe_Optimization/tree/main/documents/Papers%20with%20notes) and their theoretical results.
2. Implement the Away-Steps Frank-Wolfe algorithm from [Lacoste-Julien et al., 2015](./docs/Papers%20with%20notes/(1)%Lacoste-Julien%and%Jaggi,%2015.pdf).
3. Implement the Blended Pairwise Conditional Gradients (BPCG) algorithm from [Tsuji et. al., 2022](./documents/Papers%20with%20notes/(2)%Tsuji%et%al.,%2022.pdf).
4. Implement the (1+ε)-approximation to MEB algorithm from [Yildirim, 2008](./documentsPapers%20with%20notes/(3)%Yildirim,%2008.pdf).
5. Apply the MEB approach for anomaly detection (locate new points that are out of the MEB) on two real-world [datasets](https://github.com/Di40/MEB_FrankWolfe_Optimization/tree/main/datasets).

## Group Members:
- Dejan Dichoski
- [Marija Cveevska](https://github.com/marijacveevska)
- [Suleyman Erim](https://github.com/suleymanerim1)

## Project Structure
```bash
├───configs
├───datasets
├───documents
│   ├───Extra papers
│   ├───Extra theory
│   ├───Papers with notes
│   └───Report and Presentation
└───src
│   ├── data_generation.py
│   ├── execution.py
│   ├── FrankWolfeVariants.py
│   ├── logger.py
│   ├── plotting.py
│   ├── utils.py
├── main.py
├── setup.py
└── requirements.txt
```

## Setup
```
$ conda update conda -y
$ conda create -p venv python==3.10 -y
$ conda activate venv/
```
Go to the requirements.txt file and uncomment the symbol (#) before "-e .". Then:
```
$ pip install -r requirements.txt
```

## Usage
Choose a configuration file (.yaml) to run an experiment from the configs folder. For example:
```
$ python main.py --cfg "exp6_CustomerChurn.yaml"
```
The results will be saved to the runs/experiment folder.

## Contributing
We invite you to explore our analysis, learn from our findings, and adapt our methodologies to your own projects. Your feedback and contributions are highly valued!
