<template>
    <section class="section">
        <p class="title m-5 pt-5">Tablevision data</p>
        <div class="columns is-vcentered">
            <div class="column is-5">
                <div class="card has-background-info-light">
                    <div class="card-content">
                        <p class="title">Occupancy vs Self-Returns</p>
                        <b-field label="Select a date">
                        <b-datepicker
                            placeholder="Click to select..."
                            v-model="date"
                            :min-date="minDate"
                            :max-date="maxDate"
                        >
                        </b-datepicker>
                        </b-field>
                        <line-chart
                            ref="tablevisionChart"
                            :chartData="this.tablevisionChartData"
                        />
                    </div>
                </div>
            </div>
            <div class="column is-7">
                <div class="card has-background-primary-light mb-5">
                    <div class="card-content">
                        <p class="title">Table occupancy</p>
                        <p class="has-text-weight-bold">
                            API Status:
                            <span :class="tableVisionAPIStatus == 'LIVE' ? 'has-text-success' : 'has-text-danger'">{{ this.tableVisionAPIStatus }}</span>
                        </p>
                        <b-tag :type="leTable.state == 0 ? 'is-success' : leTable.state == 1 ? 'is-warning' : 'is-danger'" class="my-2 mx-2" size="is-large" :id="leTable.table" v-for="leTable in tables" v-bind:key="leTable.table">
                            <p class="has-text-weight-bold">{{ leTable.table }}</p>
                        </b-tag>
                        <br />
                        <p class="subtitle has-text-left mt-5">Legend</p>
                        <b-tag type="is-success" size="is-small">
                            <p>Vacant</p>
                        </b-tag>
                        <b-tag type="is-warning" size="is-small">
                            <p>Vacant but uncleared</p>
                        </b-tag>
                        <b-tag type="is-danger" size="is-small">
                            <p>Occupied</p>
                        </b-tag>
                    </div>
                </div>
                <div class="tile is-ancestor">
                    <div class="tile is-vertical is-block-tablet">
                        <div class="tile is-parent is-vertical">
                            <card-widget
                            class="tile is-child notification has-background-success-light"
                            type="is-dark"
                            icon="charity"
                            :number="this.selfReturnsPercentage"
                            suffix="%"
                            label="Self-returns rate today"
                            description="Percentage of patrons who cleaned up their tables after eating today"
                            />
                            <card-widget
                            class="tile is-child notification has-background-danger-light"
                            type="is-dark"
                            icon="silverware-clean"
                            :number="this.cleanerReturnPercentage"
                            suffix="%"
                            label="Tables cleared by cleaners today"
                            description="Tables cleared by cleaners today"
                            />
                            <card-widget
                            class="tile is-child notification has-background-warning-light"
                            type="is-dark"
                            icon="account-multiple-minus"
                            :number="'--'"
                            suffix="pm"
                            label="Peak lazy patron hours"
                            description="Time when people self-returned trays least"
                            />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import CardWidget from "@/components/CardWidget"
import CardComponent from "@/components/CardComponent"
import LineChart from "@/components/LineChart"
import API from "@/constants/api"
import PieChart from "@/components/PieChart"

export default {
    components: {
        CardWidget,
        CardComponent,
    },

    watch: {
        date: function() {
            this.fetchStatsByHour()
        },

        hourlyStats: function() {
            this.$refs.tablevisionChart.renderChart(this.tablevisionChartData);
        }
    },

    data() {
        var today = new Date()
        return {
            tableVisionAPIStatus: "Offline",
            tables: [],

            selfReturnsPercentage: 0.0,
            cleanerReturnPercentage: 0.0,
            peakLazyReturns: 0,
            totalOccupancy: 0,

            hourlyStats: [],

            date: new Date(),
            minDate: new Date(
                today.getFullYear() - 80,
                today.getMonth(),
                today.getDate()
            ),
            maxDate: new Date(
                today.getFullYear() + 18,
                today.getMonth(),
                today.getDate()
            ),

            tablevisionChartData: {
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
                    "19:00"
                ],
                datasets: [
                    {
                        label: "Cleaner returns",
                        BackgroundColor: "white",
                        borderWidth: 3,
                        borderColor: "#ef4250",
                        pointBorderColor: "#249EBF",
                        data: [],
                    },
                    {
                        label: "Self returns",
                        BackgroundColor: "white",
                        borderWidth: 3,
                        borderColor: "#7AD7F0",
                        pointBorderColor: "#7AD7F0",
                        data: [],
                    },
                ],
            },

            datasets: [
                {
                    label: "Cleaner returns",
                    BackgroundColor: "white",
                    borderWidth: 3,
                    borderColor: "#ef4250",
                    pointBorderColor: "#249EBF",
                    data: [],
                },
                {
                    label: "Self returns",
                    BackgroundColor: "white",
                    borderWidth: 3,
                    borderColor: "#7AD7F0",
                    pointBorderColor: "#7AD7F0",
                    data: [],
                },
            ],
        }
    },

    mounted() {
        this.fetchStatsByHour()
    },

    methods: {
        startAPIPolling(start) {
            // call fetch for the first time
            if (!start) {
                clearInterval(this.interval)
            } else {
                this.fetchTableVacancy()

                // continue polling after that
                this.interval = setInterval(() => {
                    this.fetchTableVacancy()
                    this.fetchTotalStats()
                }, 1000)
            }
        },
        fetchTotalStats() {
            var dateSelected = this.getStringFormattedDate(this.date)
            let r = this.$axios
            .get(API.BASE + API.TABLEVISIONSTATS + "/" + dateSelected.toString())
            .then((apiResponse) => {
                var data = apiResponse.data
                this.selfReturnsPercentage = data.self
                this.cleanerReturnPercentage = data.cleaner
                this.totalOccupancy = data.total
            }).catch((error) => {
                this.selfReturnsPercentage = 0.0
                this.cleanerReturnPercentage = 0.0
                this.totalOccupancy = 0
                if (error.response != undefined) {
                    var response = error.response.data
                    this.toastAlert(response.message, "is-danger", 5000)
                    console.log("table stats " + response.message)
                } else {
                    if (this.tableVisionAPIStatus != "Offline") {
                    this.toastAlert(error, "is-danger", 5000)
                    console.log("table stats " + error)
                    }
                }
            })
        },
        fetchStatsByHour() {
            // var cleanerData = this.tablevisionChartData.datasets[0].data
            // var selfReturnsData = this.tablevisionChartData.datasets[1].data
            // cleaner data
            this.tablevisionChartData.datasets[0].data = []
            // self returns data
            this.tablevisionChartData.datasets[1].data = []

            var dateSelected = this.getStringFormattedDate(this.date)

            let r = this.$axios
            .get(API.BASE + API.TABLEVISIONSTATS + "/per_hour/" + dateSelected)
            .then((apiResponse) => {
                var stats = new Object(apiResponse.data)
                this.hourlyStats = stats

                for (var hour in stats) {
                    console.log
                    if (stats[hour].total != 0) {
                        this.tablevisionChartData.datasets[0].data.push(stats[hour].cleaner_count)
                        this.tablevisionChartData.datasets[1].data.push(stats[hour].self_count)
                    }
                }
            })
            .catch((error) => {
                this.tableVisionAPIStatus = "Offline"
                this.tables = []
                if (error.response != undefined) {
                    var response = error.response.data
                    this.toastAlert(response.message, "is-danger", 5000)
                    console.log("table vision stats hourly " + response.message)
                } else {
                    this.toastAlert(error, "is-danger", 5000)
                    console.log("table vision stats hour" + error)
                }
            })
        },
        getTodayDate() {
            function pad(s) { return (s < 10) ? '0' + s : s; }
            var d = new Date()
            return [pad(d.getDate()), pad(d.getMonth()+1), d.getFullYear()].join('-')
        },
        getStringFormattedDate(date) {
            function pad(s) { return (s < 10) ? '0' + s : s; }
            var d = date
            return [pad(d.getDate()), pad(d.getMonth()+1), d.getFullYear()].join('-')
        },
        fetchTableVacancy() {
            let r = this.$axios
            .get(API.BASE + API.TABLEVISION)
            .then((apiResponse) => {
                var data = apiResponse.data
                this.tables = data.tables
                this.tableVisionAPIStatus = "LIVE"
            })
            .catch((error) => {
                this.tableVisionAPIStatus = "Offline"
                this.tables = []
                if (error.response != undefined) {
                    var response = error.response.data
                    this.toastAlert(response.message, "is-danger", 5000)
                    console.log("table vision " + response.message)
                } else {
                    if (this.tableVisionAPIStatus != "Offline") {
                    this.toastAlert(error, "is-danger", 5000)
                    console.log("table vision " + error)
                    }
                }
            })
        },
    }
}
</script>