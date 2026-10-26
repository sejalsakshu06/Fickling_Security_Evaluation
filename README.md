# Fickling Security Evaluation

Hands-on security evaluation of [Fickling](https://github.com/trailofbits/fickling), an open-source tool for analyzing and protecting Python pickle-based machine-learning models.

## Overview

This project evaluates the security capabilities of Fickling when handling serialized machine-learning model files.

The evaluation uses a real scikit-learn house-price prediction model together with a controlled test corpus containing clean, malicious, and malformed model samples.

The goal was to understand what Fickling can detect, what it can prevent, and where its limitations appear in practical testing.

## Objectives

- Evaluate detection of malicious pickle payloads
- Test protection against payload execution
- Test model integrity verification
- Test trusted-model allowlisting
- Compare protected and unprotected model loading
- Test multiple pickle protocol versions
- Test PyTorch model samples
- Test malformed model files
- Automate security checks using pytest
- Document findings and limitations

## Test Environment

- Python
- Fickling 0.1.12
- scikit-learn
- PyTorch
- Joblib
- pytest
- Python Pickle

## Test Corpus

The evaluation corpus contains three main categories:

### Clean

Legitimate model files and serialization samples used to verify that security controls do not incorrectly block expected files.

### Malicious

Controlled malicious model samples containing payloads designed to demonstrate unsafe behavior during deserialization.

### Malformed

Invalid or corrupted model files used to evaluate handling of malformed input.

## Testing Approach

The evaluation followed a controlled security-testing workflow:

1. Train a real machine-learning model.
2. Create clean model artifacts.
3. Create controlled malicious and malformed samples.
4. Verify malicious behavior in an isolated test environment.
5. Test the samples using Fickling security mechanisms.
6. Compare results with normal `pickle.load` behavior.
7. Automate expected behavior using pytest.
8. Record results and limitations.

## Results

The evaluation included **73 automated tests**.

Key observations from the evaluation:

- **7/7** obvious malicious samples were flagged.
- **0/7** malicious payloads executed when Fickling protection was enabled.
- **7/7** malicious payloads executed under the unprotected `pickle.load` control.
- Poisoned-weight detection was not successful.
- A clean scikit-learn model produced a false positive.
- Protocol 5 and some Joblib samples had compatibility limitations.

## Security Controls Evaluated

### Fickling Analysis

Model files were analyzed to determine whether suspicious or malicious pickle operations could be detected.

### Runtime Protection

Protected loading was compared against normal `pickle.load` behavior to determine whether malicious payload execution could be prevented.

### Integrity Verification

SHA-256 integrity checks were used to verify that a trusted model had not been modified.

### Trusted Model Allowlisting

A trusted model was used as a reference for controlled model-loading protection.

## Project Structure

```text
Fickling_Security_Evaluation/
│
├── README.md
├── .gitignore
├── requirements.txt
│
├── docs/
│   └── Fickling_House_Model_Evaluation_Documentation.docx
│
├── results/
│   ├── malicious_safety.json
│   └── safety_results.json
│
├── samples/
│   ├── clean/
│   ├── malicious/
│   └── malformed/
│
├── src/
│   ├── house_data.csv
│   ├── load_model.py
│   ├── train_house_model.py
│   └── train_model.py
│
└── tests/
    ├── test_fickling_load.py
    └── test_pytorch_injection.py