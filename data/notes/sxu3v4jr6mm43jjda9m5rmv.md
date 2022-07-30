
# [Idyll Documentation | An overview.](https://idyll-lang.org/docs)

## Introduction

Idyll can be used to create [explorable explanations](https://explorabl.es/), write data-driven stories, and add interactivity to blog engines and content management systems. The tool can generate standalone webpages or be embedded in existing pages. Choose from built-in themes or provide custom CSS.

![/static/images/fugazi.gif](https://idyll-lang.org/static/images/fugazi.gif)

We offer a [free public hosting service](https://idyll.pub/) so that you can publish your creations to the web in a matter of seconds. Continue reading to learn more about the project, or see our [example gallery](https://idyll-lang.org/gallery).

Idyll starts with the same principles as markdown, and uses a lot of the same syntax. If you want text to appear in your output, just start writing. The real power of Idyll comes when you want to use JavaScript to enrich your writing. Special syntax allows you to embed JavaScript inline with your text. Idyll comes with a variety of components that can be used out-of-the-box to create rich documents.

To include a JavaScript component, you can add tags to your text like this:

```
Lorem ipsum...

[ComponentName property:variableValue onEvent:`variableValue = 5` /]

Lorem ipsum...
```

Each tag corresponds to a React component, which receives the provided properties. Properties can be reactive variables or expressions, Idyll handles the logic to watch for variable updates and re-render components as needed. Idyll is compatible with graphics libraries like D3 and P5 and can support most JavaScript libraries that are available on npm.

## Example Usage

Idyll includes a number of useful components by default, for example here is a chart component, plotting a sine wave.

1.02.03.04.05.06.0\-1.0\-0.50.51.0

```
[Chart
  equation:` (t) => Math.sin(t)`
  domain:`[0, 2 * Math.PI]`
  samplePoints:1000 /]
```

Currently it’s static, but variables can be used to parameterize the output, allowing the chart to dynamically update. For example, we can give it a variable domain, and a variable function to plot.

```
[var name:"func" value:`Math.sin` /]
[var name:"domainStart" value:0 /]
[var name:"domainEnd" value:`2 * Math.PI` /]

[Chart
  equation:` (t) => func(t)`
  domain:`[domainStart, domainEnd]`
  samplePoints:1000 /]
```

These variables can be updated based on user actions, for example they can be attached to a button click:

1.02.03.04.05.06.0\-1.0\-0.50.51.0

```

[Chart ... /]

[Button onClick:`func = Math.sin`]sin[/Button]
[Button onClick:`func = Math.cos`]cos[/Button]
```

or bound to the value of standard input widgets:

1.02.03.04.05.06.0\-1.0\-0.50.51.0

#### Update Domain

Start:

End:

```
[Chart ... /]

#### Update Domain

Start: [Range value:domainStart min:`-4 * Math.PI` max:0 step:0.01  /]
End: [Range value:domainEnd min:0 max:`4 * Math.PI` step:0.01  /]
```

Write your own equation:

1.02.03.04.05.06.0\-3.0\-2.0\-1.01.02.03.0

#### Update Domain

Start:

End:

```

[var name:"funcString" value:`"(x) => x * Math.sin(10 / (x || 1))"` /]
[derived name:"funcFromString" value:`eval(funcString)` /]

[TextInput value:funcString /]

[Chart
  equation:` (t) =>  funcFromString(t) `
  domain:`[domainStart, domainEnd]`
  range:`[-3, 3]`
  samplePoints:1000 /]
```

## Support

If you like what Idyll is doing, consider [buying a sticker](https://opencollective.com/idyll) to help sustain the project, or select from one of the other one-time and recurring donation options on Open Collective.

[![](https://opencollective.com/idyll/donate/button@2x.png?color=blue)](https://opencollective.com/idyll/)

Idyll is supported by the Interactive Data Lab at the University of Washington, and by O’Reilly Media, Rhizome and The Eutopia Foundation.![sponsors](inbox/assets/sponsors..png)
