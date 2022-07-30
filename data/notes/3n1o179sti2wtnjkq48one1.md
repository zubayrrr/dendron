
AWS CodePipeline is a completely managed continuous delivery service(with manual approval) that assists you in automating your release pipelines for quick and reliable application and infrastructure changes.

Based on the release model you set, CodePipeline automates the build, test, and deploy parts of your release process every time there is a code change. This allows you to provide features and upgrades quickly and consistently. AWS CodePipeline can be easily integrated with third-party services like GitHub or your own custom plugin. You only pay for what you use with AWS CodePipeline. There are no hidden costs or long-term obligations. — via [AWS CodePipeline - Coding Ninjas CodeStudio](https://www.codingninjas.com/codestudio/library/aws-codepipeline)

- Automatic
  - From the check-in of your code to the deployment on to your servers, CodePipeline takes care of the entire process.
- Easy to setup
  - CodePipeline has no servers to provision, it's dead simple to configure and get working. There are pre-built plugins or you can roll your own.
- Configurable
  - You can create, configure and modify all stages of your software release process with ease. You can implement automated testing and customize the deployment process.

CodeCommit is not the only repository you can use with [[devlog.AWS CodePipeline]], such as [[devlog.AWS S3]], Github, Bitbucket and Github Enterprise.

- You need an [[devlog.AWS IAM]] user with right policies attached to it.

Create Pipeline

![](https://res.cloudinary.com/zubayr/image/upload/v1655279967/wiki/cavxaueres9g0y82ejum.png)

Unlike [[devlog.AWS CodeDeploy]] it supports [[devlog.AWS CodeCommit]] so you can choose your Source as such.

![](https://res.cloudinary.com/zubayr/image/upload/v1655280066/wiki/ofw8mz5jopulafyhazzk.png)

You can use [[devlog.AWS S3]] as a source too with change detection options.

You can add a build stage if your application requires compiling or you can skip to deploy stage.

![](https://res.cloudinary.com/zubayr/image/upload/v1655540479/wiki/ehjwkvx8qcvu0dxznclg.png)

![](https://res.cloudinary.com/zubayr/image/upload/v1655280123/wiki/kduzm8nljigeq2dupxos.png)

## Code Pipeline with [[devlog.AWS CodeBuild]]

CodeBuild can be used in both build and test stages of a pipeline. You can add CodeBuild build action to a pipeline as well as CodeBuild test action.

## Versioning

CodePipeline uses the ETag to manage and understand the flow so far for that execution of the pipeline. CodePipeline can have multiple executions at the same time. So, it needs to have a way to identify when version of the artifact is tied to which execution.

## Managing CodePipeline

- View logs for debugging
- Edit/Add Stages -> Action providers
- Toggle transitions
- Retry failed stages
- Delete

## Approval Action

- Setup approvers in [[devlog.AWS IAM]] via managed policy: **AWSCodePipelineApproverAccess** (from Action Provider in a stage)

## CodePipeline with [[devlog.AWS EventBridge]]

- Events can come from multiple stages within the pipeline.
- EventBridge can watch over events and trigger [[devlog.AWS SNS]] topic based on it.
- EventBridge can work with [[devlog.AWS Lambda]] at source stage. It can work with SNS at the build or deploy stages.

![](https://res.cloudinary.com/zubayr/image/upload/v1655544508/wiki/rvmsyahweeycgtzonaav.png)
