# Python Microframeworks on Onion Architecture

![A flask on a bed of onions](https://github.com/hbibel/flask_onion/blob/main/flask_onion.jpeg?raw=true)

A showcase template on how to build Flask / FastAPI applications using the [Onion Architecture](https://jeffreypalermo.com/2008/07/the-onion-architecture-part-1/).

Switch to the `fastapi` branch to see the FastAPI implementation.

## Motivation

Microframeworks like Flask and FastAPI offer a convenient set of tools for building web applications. They consciously leave many decisions to the developer. This makes it easy to get started and offers flexibility as well as a joyful learning curve, where you learn as your application grows. If you are not careful however, this poses the risk - especially for projects that far outgrow their initially intended scope - to build a code base that proves hard to maintain in the long run. This project contains a simple implementation of the popular Onion Architecture that should give you a good starting point for your next Flask or FastAPI project.

## Layers

Layers only depend on other layers below. In this project, layers are represented by packages:

```
--------------------
        app
--------------------
   infrastructure
--------------------
application_services
--------------------
  domain_services
--------------------
       domain
--------------------
```

Principles:

- never import from an outer layer
- pass dependencies through constructor arguments (constructor injection) in Flask or use dependency injection in FastAPI
