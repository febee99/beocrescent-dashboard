<template>
    <section>
    <div class="columns is-vcentered is-multiline">
        <div class="column is-4">
            <card-text
                class="tile is-child"
                label="Basic Information"
                information="1) Team 6 data starts from 10am to 3pm.
2) Team 7 data starts from 9am to 4pm
3) We took the percentage of Positive tray return rates over time
   using all the days of data collected.
4) Difference in both team’s positive tray return rate is due the
   difference in how we collect data."
            />
        </div>
        <div class="column is-4">
            <card-text
                class="tile is-child"
                label="Analysis"
                information="1) Tray return rate during peak hours (Around 11pm to 2pm)
   is lower than during non-peak periods. 
   
   
   
   "
            />
        </div>
        <div class="column is-4">
            <card-text
                class="tile is-child"
                label="Reasons"
                information="1) Cleaners are more active in clearing tables to 
   allow other diners to use the tables during peak periods.
2) During peak periods, it maybe harder to navigate to tray return
   points hence patrons are less likely to clear.
   
   "
            />
        </div>
        <div class="column is-12">
            <div class="card">
                <div class="card-content">
                    <p class="title">Positive Tray Return Rate (%) Consolidated Data</p>
                    <line-chart :chartData="this.cleanerReturnInsights"/>
                </div>
            </div>
        </div>
       
      </div>    
 
    <div class="columns is-12">
        <div class="card">
            <div class="card-content">
                <p class="title is-size-5-touch">Hourly Tray Return Rate</p>
                <!-- <b-field label="Select a date">
                <b-datepicker
                    placeholder="Click to select..."
                    v-model="date"
                    :min-date="minDate"
                    :max-date="maxDate"
                >
                </b-datepicker>
                </b-field> -->
                <line-chart
                    ref="overallRateLineChart"
                    :chartData="this.patronReturnInsights"
                />
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
            title: 'Beo Crescent IoT Dashboard',
            lineChartAPIStatus: "Offline",
            lineChartTable: [],
            interval: null,
            trayReturnInsights: {
                labels: ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
                datasets: [
                    {
                        backgroundColor: ['#ee4350', '#409cd2', '#80257d', '#bfd2fb', '#d6006d', '#f5a167', '#AEE1CD'],
                        pointBackgroundColor: 'white',
                        borderWidth: 1,
                        pointBorderColor: '#249EBF',
                        data: [60, 200, 100, 250, 300, 500, 140]
                    }
                ]
            },
            cleanerReturnInsights: {
                labels: ['06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00'],
                datasets: [
                    {  
                        label: "Nan Yuan Fishball Noodle Stall",
                        backgroundColor: ['#409cd2'],
                        pointBackgroundColor: 'white',
                        borderWidth: 1,
                        pointBorderColor: '#249EBF',
                        data: [10, 30, 46, 44, 55, 44, 61, 44, 22, 34, 15, 23, 25, 12, 44]
                    }
                ]
            },
            patronReturnInsights: {
                labels: [
                "04:00",
                "05:00",
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
                        label: "Group 6",
                        BackgroundColor: "#white",
                        borderWidth: 3,
                        borderColor: "#7AD7F0",
                        pointBorderColor: "#7AD7F0",
                        data: [],
                    },
                    {
                        label: "Group 7",
                        BackgroundColor: "#white",
                        borderWidth: 3,
                        borderColor: "#7AD7F0",
                        pointBorderColor: "#7AD7F0",
                        data: [],
                    },
                ],
            },
        }
    },
    watch: {
        lineChartTable: function () {
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
            }
        },
        getLineChartData() {
            let group6 = this.$axios
                .get(API.BASE + API.G6OVERVIEW)
                .then((apiResponse) => {
                    var data = apiResponse.data;
                    for (var time of Object.keys(data)) {
                        var data1 = data[time];
                        this.lineChartTable.push(data1);
                        this.patronReturnInsights.datasets[0].data.push(data1);
                    }
                    this.lineChartAPIStatus = "LIVE";
                });

            let group7 = this.$axios
                .get(API.BASE + API.G6OVERVIEW)
                .then((apiResponse) => {
                    var data = apiResponse.data;
                    //console.log(Object.keys(time_sensor_data));
                    for (var time of Object.keys(data)) {
                        //console.log(time);
                        var data1 = data[time];
                        this.lineChartTable.push(data1);
                        this.patronReturnInsights.datasets[1].data.push(data1);

                    }

                    this.lineChartAPIStatus = "LIVE";
                })
                .catch((error) => {
                    this.lineChartAPIStatus = "Offline";
                    this.lineChartTable = [];
                    if (error.response != undefined) {
                        var response = error.response.data;
                        this.toastAlert(response.message, "is-danger", 5000);
                        console.log("overviewrate " + response.message);
                    } else {
                        if (this.lineChartAPIStatus != "Offline") {
                        this.toastAlert(error, "is-danger", 5000);
                        console.log("overviewrate " + error);
                        }
                    }
                });

        },
    },
}
</script>