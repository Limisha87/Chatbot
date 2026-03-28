# Jekyll homepage

To run locally:

```bash
cd jekyll_homepage
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000.

To deploy to GitHub Pages:
1) Create repo `yourname.github.io`.
2) `git init && git add . && git commit -m "init"`
3) `git remote add origin https://github.com/yourname/yourname.github.io.git`
4) `git push -u origin main`
5) In GitHub repo settings, enable Pages from `main` branch.

Your site will be at `https://yourname.github.io`.
