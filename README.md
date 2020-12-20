# Reference document database prototype app

This application is implemented as a lab project of the course **SW development techniques (Ohjelmistotekniikka)** at the *University of Helsinki*. The purpose of the application is to experiment with a prototype of a reference database. The reference database assists identifying and providing documentation of historical business cases as a basis of tendering process. The application is a prototype for potential commercial product to be utilized in a organization with thousands of business engagements annually.

The user of the application may upload commercial documents into the database. The documents may be then browsed and searched based on the provided document classification and full-text search. User may then download the most applicable commercial documents to be used as a benchmark for the new business opportunity.

## Technical requirements
The application has been tested in following operating systems:
- Windows 10 v. 10.0.17134 (build 17134)
- Ubuntu 18.04.5 LTS

Application has been developed and tested with Python version
- `3.9.0`

## Documentation

- [User manual](https://github.com/roopekole/ohte-harjoitustyo/blob/master/app/documentation/user_manual.md)
- [Software architecture](https://github.com/roopekole/ohte-harjoitustyo/blob/master/app/documentation/software_architecture.md)
- [Application requirements](https://github.com/roopekole/ohte-harjoitustyo/blob/master/app/documentation/application_requirements.md)
- [Test documentation](https://github.com/roopekole/ohte-harjoitustyo/blob/master/app/documentation/test_document.md)
- [Workhour log](https://github.com/roopekole/ohte-harjoitustyo/blob/master/app/documentation/workhour_log.md)

## Current release
[Final release](https://github.com/roopekole/ohte-harjoitustyo/releases/tag/v1.0)
 

## Get started

1. Install dependencies:

```bash
python3 -m pipenv install
```

2. Initialize the program

```bash
python3 -m pipenv run build
```

3. Run the app:

```bash
python3 -m pipenv run start
```

## Command prompt convenience commands:

**Run the app**:

```bash
python3 -m pipenv run start
```

**Perform unit testing**:

```bash
python3 -m pipenv run test
```

**Run the test coverage**:

```bash
python3 -m pipenv run coverage
```

**Generate test coverage report**:

```bash
python3 -m pipenv run coverage-report
```

Report is generated to *htmlcov* directory.

Configurations are set in file [.coveragerc](https://github.com/roopekole/ohte-harjoitustyo/blob/master/app/.coveragerc).

### Pylint

Pylint code analysis can be initated:

```bash
python3 -m pipenv run lint
```

Configurations are set in file [.pylintrc](https://github.com/roopekole/ohte-harjoitustyo/blob/master/app/.pylintrc).
