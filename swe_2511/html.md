# HTML & CSS

## Markup languages

- made in the 1960s

- Procedural Vs Descriptive Markup languages 
- browsers might support different versions, or parts of different versions of HTML
  - for example, the video tag used to be not very supported
- HTML is a descriptive markup language

  There might be quiz questions on the order of the tags
  "what should be the font style"

## CSS

- you don't need to use pseudo classes with class selectors specifically, you can use them with any selector. 

- The cascade priority determines which source of style takes precedence when there are conflicting styles. The priority, from lowest to highest, is:

  User-agent (browser) style sheets: These are the browser's default settings.
  Reader style sheets: These are set by the user, for example, through a browser extension.
  Author style sheets: These are the styles defined by the website's author in external or imported style sheets.
  !important specifications: An !important declaration overrides other styles.

- Specificity is used to resolve conflicts when multiple rules within the same group target the same element. A three-digit number can be used to calculate specificity, with the highest number winning.

  IDs: Get one point for each ID in the selector. ID selectors have the highest priority.
  Classes & Pseudo-classes: Get one point for each class or pseudo-class in the selector.
  Element Names: Get one point for each element name in the selector. These have the lowest priority.

- Some HTML elements are only allowed to be used once per page, eg: <main>, and <h1>. With only one of these elements guaranteed per page, it's safe to select them with a simple element selector. But this makes things harder down the line
- from my online research, you should avoid selecting by tag, and mostly select by class. You really only need id’s when you have to target a very specific element for js, but classes apply to every instance of that element mainly for styling purposes. You can cause weird shit in js if you have multiples of the same id, or if you target something by a class and multiples of that class exist on the page. IDs can also help with unit testing, for example it makes the selenium xpath thing easier.
  
  - I see comments like, "I typically use ids only when I need access to that element with JavaScript, if it's styling and I can't do it with a class, I've not been clever enough with my selectors and they are not cascading properly, then it's refactor time."
  - "If we are talking about CSS styling. I would highly suggest just never using ID. Even if you have one component just use class. Id is useful not so much for styling, but for uniquely identifying components in the browser. Which can have its uses but in terms of styling I would say using ID is generally considered an anti pattern."

  - [One of CSS lint rules is: "It's better to not use IDs in selectors". ](https://github.com/CSSLint/csslint/wiki/rules)