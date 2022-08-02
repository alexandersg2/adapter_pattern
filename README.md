# Adapter Pattern

The Adapter pattern is a structural design pattern that allows objects with incompatible interfaces to work together.

It allows you to create a middle-layer "adapter" class that acts as a translator between your code and a class with an incompatible interface.

Use the Adapter class when you want to use an existing, unmodifiable class, but its interface isn’t compatible with the rest of your code. It's often useful when working with 3rd-party libraries.

### Pros:
- Single Responsibility Principle - You can separate the interface or data conversion code from the primary business logic of the program.
- Open/Closed Principle - You can introduce new types of adapters into the program without breaking the existing client code, as long as they work with the adapters through the client interface.

### Cons:
The overall complexity of the code increases because you need to introduce a set of new interfaces and classes. Sometimes it’s simpler just to change the service class so that it matches the rest of your code (if possible).


## The example:
This example looks at a notification client that can compose and send emails.

Imagine that we get a new requirement that allows users to enter their phone number instead of their email address, and receive SMS messages instead of emails. The SMS messages must be sent in exactly the same way as the emails. We plan to use an external service and it's package to achieve this. However, the interface the code uses isn't compatible with our client code.

One possible solution would be to update our client code, but perhaps this isn't practical or possible. So, maybe we can update the package? Nope, also not possible. Well, this is where the Adapter Pattern comes in.

We will create a new middle-layer class, SMSMessageAdapter, that implements the Email interface (no actual interface used in this example, for simplicity's sake and... Python!). This middle layer will be accessed by the client code and will make "adapted calls" to the SMSMessage class.

## Class Diagram:

![Class Diagram](./class_diagram.png?raw=true "Adapter Pattern")