<template>
    <section>
        <b-loading :is-full-page="true" v-model="isLoading" :can-cancel="false"></b-loading>
    <div class="tile is-ancestor is-block-tablet is-flex-widescreen" style="overflow-x: auto;">
        <div class="tile is-parent ">
            <card-text
                class="tile is-child"
                label="Basic Information"
                information="1) Team 6 data starts from 10am to 3pm.
2) Team 7 data starts from 9am to 4pm
3) We took the percentage of positive tray 
return rates over time using all the days 
of data collected.
4) Difference in both team’s positive tray 
return rate is due to the difference in 
how we collect data."
            />
        </div>
        <div class="tile is-parent ">
            <card-text
                class="tile is-child"
                label="Analysis"
                information="1) Tray return rate during peak hours 
(Around 11pm to 2pm) is lower than during 
non-peak periods. 
   
   
   
   "
            />
        </div>
        <div class="tile is-parent ">
            <card-text
                class="tile is-child box"
                label="Reasons"
                information="1) Cleaners are more active in clearing 
tables to allow other diners to use the 
tables during peak periods.
2) During peak periods, it maybe harder to 
navigate to tray return points hence 
patrons are less likely to clear.
   
   "
            />
        </div>
    </div>

    <div class="columns is-vcentered is-multiline">

        <div class="column is-5">
            <div class="card">
                <div class="card-content">
                    <p class="title">Positive Tray Return Rate (%) Consolidated Data</p>
                    <line-chart ref="overallRateLineChart" :chartData="this.patronReturnInsights"/>
                </div>
            </div>
        </div>

        <div class="tile is-ancestor">
                    <div class="tile is-vertical is-block-tablet">
                        <div class="tile is-parent is-vertical">
                            <card-widget
                            class="tile is-child notification has-background-success-light"
                            type="is-dark"
                            :number="g7tr"
                            suffix="%"
                            label="G7 Tray Return"
                            description="Percentage of patrons who cleaned up their tables after eating (G7 Tray Return)"
                            />
                            <card-widget
                            class="tile is-child notification has-background-danger-light"
                            type="is-dark"
                            :number="g7tb"
                            suffix="%"
                            label="G7 Tablevision"
                            description="Percentage of patrons who cleaned up their tables after eating (G7 Tablevision)"
                            />
                            <card-widget
                            class="tile is-child notification has-background-info-light"
                            type="is-dark"
                            :number="g6"
                            :suffix="'%'"
                            label="G6 Tray Return"
                            description="Percentage of patrons who cleaned up their tables after eating (G6 Tray Return)"
                            />
                        </div>
                    </div>
                </div>
    </div>
       
          
    </section>
</template>

<script>
import CardWidget from '@/components/CardWidget'
import CardComponent from '@/components/CardComponent'
import DoughnutChart from '@/components/DoughnutChart'
import LineChart from '@/components/LineChart'
import PieChart from '@/components/PieChart'
import CardText from '@/components/CardTextComponent'
import API from "@/constants/api";

export default {

    head() {
        return {
            title: this.title,
        }
    },

    components: {
        CardWidget,
        DoughnutChart,
        CardText
    },
    
    data() {
        return {
            g7tr: '',
            g7tb: '',
            g6: '',
            isLoading: true,
            title: 'Beo Crescent IoT Dashboard',
            lineChartAPIStatus: "Offline",
            lineChartTable: [],
            interval: null,
            patronReturnInsights: {
                // labels: ['04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'],
                labels: ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00'],
                datasets: [
                    {
                    type: 'line',
                    label: 'G7-Tray-Return',
                    fill: false,
                    borderColor: '#23d160',
                    data: [0]
                    }, {
                    type: 'line',
                    label: 'G7-Tablevision',
                    borderColor: '#ff3860',
                    fill: false,
                    data: [0]
                    }, {
                    type: 'line',
                    label: 'G6-Tray-Return',
                    borderColor: '#209cee',
                    fill: false,
                    data: [0]
                    }
          ]
            },
        }
    },
    watch: {
        patronReturnInsights: function () {
            this.$refs.overallRateLineChart.renderChart(this.patronReturnInsights);
        }
    },
    methods: {
        startAPIPolling(start) {
        // call fetch for the first time
            if (!start) {
                clearInterval(this.interval);
            } else {
                this.getLineChartData();
                this.populateData();
            }
        },
        getLineChartData() {
            this.patronReturnInsights.datasets[0].data = [0]
            this.patronReturnInsights.datasets[1].data = [0]
            this.patronReturnInsights.datasets[2].data = [0]
            let something = this.$axios
                .get(API.BASE + API.OVERVIEW)
                .then((apiResponse) => {
                    var data = apiResponse.data;
                    
                    let g6 = data.g6
                    let g7tr = data['g7-tray']
                    let g7tb = data['g7-tablevision']


                    for (var key in g6) {
                        let t = parseInt(key)
                        if (t > 9 && t <= 15) {
                            this.patronReturnInsights.datasets[0].data.push(g7tr[key]);
                            this.patronReturnInsights.datasets[1].data.push(g7tb[key]);
                            this.patronReturnInsights.datasets[2].data.push(g6[key]);
                        } else if (t > 15 && t < 20) {
                            this.patronReturnInsights.datasets[1].data.push(g7tb[key]);
                        }
                    }


                    this.$refs.overallRateLineChart.renderChart(this.patronReturnInsights);
                    this.isLoading = false;
                    this.lineChartAPIStatus = "LIVE";
                });
        },

        populateData() {
            let somethingelse = this.$axios
                .get(API.BASE + API.OVERVIEW2)
                .then((apiResponse) => {
                    var data = apiResponse.data;
                    
                    this.g6 = data.g6
                    this.g7tr = data.g7tr
                    this.g7tb = data.g7tb
                });
        }
    }
}
</script>