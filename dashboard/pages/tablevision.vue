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
                        ref="nanyuanLineChart"
                        :chartData="this.cleanerReturnInsights"
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
                            label="Self-returns rate"
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
        selfReturnsPercentage: function() {

        },
    },

    data() {
        return {
            tableVisionAPIStatus: "Offline",
            tables: [],

            selfReturnsPercentage: 0.0,
            cleanerReturnPercentage: 0.0,
            peakLazyReturns: 0,
            totalOccupancy: 0
        }
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
                    this.fetchStatistics()
                }, 1000)
            }
        },
        fetchStatistics() {
            let r = this.$axios
            .get(API.BASE + API.TABLEVISIONSTATS)
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