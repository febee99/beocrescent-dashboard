# Development readme :rocket:

> For detailed explanation on how things work, check out [Nuxt.js docs](https://nuxtjs.org).

## Libraries

### Buefy or Bulma (CSS Framework)

The dashboard styling uses the [Buefy](https://buefy.org/documentation) framework to modularise components. Buefy is built on top of Bulma, and if components are not available in Buefy, refer to the [Bulma documentation](https://bulma.io/documentation/).

### vue-chartjs

Currently, we are using [vue-chartjs](https://vue-chartjs.org) for the data visualisation charts. You can refer to the documentation in the link and add it into the `components` folder. More on the structure below.

### Icon pack

We're using the material design icons, feel free to refer to the cheatsheet [here](https://cdn.materialdesignicons.com/5.4.55/).

## Folder structure

**assets**: You can place images here or any other static assets.

**components**: The dashboard contains the `components` folder to modularise custom components such as the chart visualisation files.

**layouts**: This is the main layout page. I doubt you will need to edit this much. The navbar and the main layout lives here.

**pages**: Edit the pages here. Since this is a Single-Paged App (SPA), we used the import statements to compartmentalise pages as the tabs.

**plugins**: `helpers.js` file is used to include the Vue mixins for global function implementations.

**static**: You can replace the `favicon.ico` file here, but honestly I'm lazy.

## Pages

To edit the page, `index.vue` is the main entry point. Other tabs are imported, for example, nanyuan.vue.

## Troubleshooting

Just contact Emmanuel: Telegram @theodorayy lol I will try my best to assist