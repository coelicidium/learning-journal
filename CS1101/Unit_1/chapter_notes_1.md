## UNIT 1 - FUNDAMENTAL CONCEPTS 

A program is a sequence - an ordered set - of finite instructions  called algorithms, provided in a formal language. 

Every program ultimately is nothing more but data that goes in (**input**), is manipulated when certain chosen conditions are met (**conditional execution**), usually performing said manipulation with math-dedicated parts of the language syntax (**arithmetic operators**, in particular).

**Type** is the term used to define as a whole the class - roughly translated here as category - and thus the properties of the inputs, also known as values. 

Common types are numeric in nature, like **integers, floats, complex numbers and booleans;** almost every type is mathematical, like **sets, arrays** (a subcategory of sets), **tuples,** then there are **characters** (single letters, numbers or symbols), **strings** (many characters), **dictionaries**, and possibly many others.  Which types a formal language has, depends on the syntax defined in the language itself.

This kind of languages is characterized by features often not present in natural, spoken/written/performed languages; on the other hand, they also have features that the latter do not have. These are **ambiguity, redundancy, and literalness.**

Formal languages have **nearly to no ambiguity at all**, and if no ambiguity is present, every statement equals one meaning that doesn't change when the context does. Redundancy is then a given: to avoid misunderstandings, we repeat ourselves, defining the meaning of words every time, as they could change when changing the context we are in and the people we talk to. 
Literalness refers to the absence of rhetorical figures: everything is exactly what it says it is. For all of these reasons, **formal languages are dense, structure-heavy** and unforgiving on the details, consequently harder to read, but with their purpose perfectly understandable even only by means of syntactical and lexical analysis of their tokens, which are lexical objects predefined as having a particular meaning.

This process of structure and token analysis is called parsing, and the program doing this, a parser. 

Since we are not perfect at all, we might make mistakes called bugs. Debugging is the act of problem solving needed to fix them.

The most common bugs can be categorized into syntax, logic and runtime errors.