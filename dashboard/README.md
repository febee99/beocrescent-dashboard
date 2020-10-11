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

To edit the page, `index.vue` is the main entry point. Other tabs are imported, for example, `nanyuan.vue`.

## Adding graphs

To display the graph, tag your `<line-chart>` with a `ref` like below:

```html
<line-chart ref="nanyuanLineChart" :chartData="this.cleanerReturnInsights" />
```

In `data()`, `cleanerReturnInsights` currently looks like this:

```
    cleanerReturnInsights: {
        labels: [
            "06:00",
            "07:00",
            "08:00",
            "09:00",
            "10:00",
            "11:00",
            "12:00",
            "13:00",
            "14:00",
            "15:00",
            "16:00",
            "17:00",
            "18:00",
            "19:00",
            "20:00",
            "21:00",
            "22:00",
            "23:00",
        ],
        datasets: [
            {
                label: "Nan Yuan Fishball Noodle Stall",
                pointBackgroundColor: "white",
                borderWidth: 3,
                pointBorderColor: "#249EBF",
                data: [], //update this
            },
        ],
    },
```

So if I were to call my API, I will want to update the `cleanerReturnInsights.datasets[0].data`, which looks like this:

```js
        // in the get_fsr_rfid_data() function in nanyuan.vue:

        for (var time of Object.keys(time_sensor_data)) {
            console.log(time);
            var data1 = time_sensor_data[time];

            // Store in a temp array first in data()
            this.rfidFsrTable.push(data1);

            // also update the datasets
            this.cleanerReturnInsights.datasets[0].data.push(data1)
        }
```

Then in the same page, go to the `watch` property in the script and watch for changes on the `rfidFsrTable` variable. If there are changes to the chart from an API call, call the `renderChart()` function:

```js
    watch: {
        rfidFsrTable: function() {
            this.$refs.nanyuanLineChart.renderChart(this.cleanerReturnInsights)
        }
    },
```

This will trigger the `renderChart()` function from the child element (`line-chart`).

> You can take a look at `nanyuan.vue` for this example.

## Troubleshooting

_Just contact Emmanuel (Telegram @theodorayy) lol I will try my best to assist_