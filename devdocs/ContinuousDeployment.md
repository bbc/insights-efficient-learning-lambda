# Continuous Deployment

Uses a Jenkins pipeline defined in the [Jenkinsfile](../Jenkinsfile)

## Stages
The pipeline is split into several stages

| Stage | Description |
| ----- | ----------- |
| Build and Test  | Builds the lambda with dev dependencies and runs the unit tests |
| Build and Package | Builds the lambda with package dependencies and creates a zip archive which is stashed for later use |
| Release | Unstashes the zip archive and uses the cosmos-release tool to release the lambda to the Cosmos repository so it can be deployed |
| Deploy to Test| Deploys the current version to the TEST environment using the Cosmos CLI|

Note: The `Build and Test` and `Build and Package` both clean the `/venv` directory to avoid pullution between stages.

## Workflow

The Pipeline is trigger via pushed changes to Branches and PullRequests

Note: The `Release` and `Deploy to Test` stages are only run on master branch

### Troubleshooting

_The release stage failed with 409 Conflict_

The most likely cause for this is the version has already been released. Check the version in setup.py against the released versions on the Cosmos UI.

## Pipeline

[Efficient Learning Pipeline](https://jenkins.education.live.tools.bbc.co.uk/job/efficient-learning-lambda/)
