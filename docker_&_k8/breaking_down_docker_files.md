# Breaking Down the docker file to image to container pipeline

A Docker image is a series of layers stacked on each other that form the dependencies and source code needed to run your application. During a Docker image build, all those layers get packaged together to produce a final Docker image.

## So what is a docker file? 

A Dockerfile is executed from top to bottom during a given docker image build. Instructions are invoked in order, and each instruction generally maps to an image layer. Those layers, stacked on top of each other one after the other, form our final Docker image. 

You can name them as just "Dockerfile" with no file extension, or if you have multiple dockerfiles in a single directory, you can give those abitrary names with the .dockerfile extension. Using the .dockerfile extension tells VSCode that the file is a DockerFile for code highlighting and linting.

## Dockerfile instructions
