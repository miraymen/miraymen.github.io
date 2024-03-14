# The Minimal Light Theme

[![LICENSE](https://img.shields.io/github/license/yaoyao-liu/minimal-light?style=flat-square&logo=creative-commons&color=EF9421)](https://github.com/yaoyao-liu/minimal-light/blob/main/LICENSE)

\[[Based on Yaoyao Liu's code](https://minimal-light-theme.yliu.me/)\]
 
Link to Yaoyao Liu's page: [[link](https://github.com/yaoyao-liu/yaoyao-liu.github.io)]

## Features

- Simple and elegant personal homepage theme
- Jekyll theme, automatically deployed by GitHub Pages
- Basic search engine optimization
- Mobile friendly
- Supporting Markdown 
- Supporting dark mode

## Project Architecture

```
.
├── _data                    
|   └── publications.yml                      # the YAML file for publications
├── _includes                    
|   ├── publications.md                       # the Markdown file for publications
|   └── services.md                           # the Markdown file for services
├── _layouts                  
|   └── homepage.html                         #  the html template for the homepage 
├── _sass
|   ├── minimal-light.scss                    #  this file will be compiled into a CSS file to control the style of the page              
|   └── minimal-light-no-dark-mode.scss       #  this file is similar to minimal-light.scss with the dark mode disabled
├── assets                                    #  some files
├── html_source_file                          #  compiled HTML files
├── .gitignore                                #  this file specifies intentionally untracked files that Git should ignore
├── CNAME                                     #  the custom domain, will be used by GitHub page sevice
├── Gemfile                                   #  a RubyGems related file
├── LICENSE                                   #  the license file
├── README.md                                 #  the readme file (English)
├── README_de.md                              #  the readme file (German)
├── README_zh_Hans.md                         #  the readme file (Simplified Chinese)
├── README_zh_Hant.md                         #  the readme file (Traditional Chinese)
├── _config.yml                               #  the Jekyll configuration file, including some options of the page  
└── index.md                                  #  the content of the index page, using Markdown
```

## License

This work is licensed under a [Creative Commons Zero v1.0 Universal](https://github.com/yaoyao-liu/minimal-light/blob/master/LICENSE) License.

## Acknowledgements

The project uses the source code from the following repositories:

* [pages-themes/minimal](https://github.com/pages-themes/minimal)

* [orderedlist/minimal](https://github.com/orderedlist/minimal)

* [al-folio](https://github.com/alshedivat/al-folio)
