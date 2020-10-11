<template>
    <section>
        <p class="title m-5 pt-5">RFID-tagged tray-returns data</p>
        <div class="columns mt-5 is-vcentered is-multiline">
            <div class="column is-4 has-text-centered">
                <div class="card">
                    <div class="card-content">
                        <line-chart :chartData="this.cleanerReturnInsights"/>
                    </div>
                </div>
            </div>
            <div class="column is-4 has-text-centered">
                <div class="card">
                    <div class="card-content">
                        <pie-chart :chartData="this.nanyuanReturns"/>
                    </div>
                </div>
            </div>
            <div class="column is-4 has-text-centered">
                <div class="card">
                    <div class="card-content">
                        <p class="title">Other data</p>
                        <card-widget
                            class="tile is-child"
                            type="is-info"
                            icon="clock"
                            :number="84"
                            suffix="%"
                            label="Self-returns rate"
                            description="Percentage of patrons who cleaned up their tables after eating today"
                        />

                <card-widget
                    class="tile is-child"
                    type="is-info"
                    icon="clock"
                    :number="84"
                    suffix="%"
                    label="Self-returns rate"
                    description="Percentage of patrons who cleaned up their tables after eating today"
                />
                    </div>
                </div>
            </div>
        </div>
        <br>
        <hr>
        <br>
        <p class="title m-5 pt-5">Tablevision data</p>
        <div class="columns mt-5 is-vcentered is-multiline">
            <div class="column is-4 has-text-centered">
                <div class="card">
                    <div class="card-content">
                        <p class="title">Table occupancy</p>
                        <p class="has-text-weight-bold">API Status: <span :class="tableVisionAPIStatus == 'LIVE' ? 'has-text-success' : 'has-text-danger'">{{this.tableVisionAPIStatus}}</span></p>
                        <b-tag :type="leTable.state == 0 ? 'is-success' : leTable.state == 1 ? 'is-warning' : 'is-danger'" class="my-2" size="is-large" :id="leTable.table" v-for="leTable in tables" v-bind:key="leTable.table">
                            <p>{{leTable.table}}</p>
                        </b-tag>
                        <br>
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
            </div>
            <div class="column is-4">
                <card-widget
                    class="tile is-child"
                    type="is-info"
                    icon="clock"
                    :number="84"
                    suffix="%"
                    label="Self-returns rate"
                    description="Percentage of patrons who cleaned up their tables after eating today"
                />
            </div>
            <div class="column is-4">
                <card-widget
                    class="tile is-child"
                    type="is-info"
                    icon="clock"
                    :number="39"
                    suffix=" occasions"
                    label="Tables cleared by cleaners today"
                    description="Tables cleared by cleaners today"
                />
            </div>
        </div>
    </section>
</template>

<script>
import CardWidget from '@/components/CardWidget'
import CardComponent from '@/components/CardComponent'
import LineChart from '@/components/LineChart'
import PieChart from '@/components/PieChart'
import API from '@/constants/api'

export default {

    components: {
        CardWidget,
        CardComponent
    },

    data() {
        return {
            tableVisionAPIStatus: "Offline",
            tables: [
            ],

            interval: null,

            nanyuanReturns: {
                labels: ['Trays not returned to cleaner trolleys', 'Trays into cleaner trolleys'],
                datasets: [
                    {
                        backgroundColor: ['#ee4350', '#409cd2'],
                        pointBackgroundColor: 'white',
                        borderWidth: 1,
                        pointBorderColor: '#249EBF',
                        data: [60, 200]
                    }
                ]
            },
            cleanerReturnInsights: {
                labels: ['06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00'],
                datasets: [
                    {  
                        label: "Nan Yuan Fishball Noodle Stall",
                        pointBackgroundColor: 'white',
                        borderWidth: 3,
                        pointBorderColor: '#249EBF',
                        data: [10, 30, 46, 44, 55, 44, 61, 44, 22, 34, 15, 23, 25, 12, 44]
                    }
                ]
            },

        }
    },

    methods: {
        startTableVisionAPIPolling(start) {
            // call fetch for the first time
            if (!start) {
                clearInterval(this.interval);
            } else {
                this.fetchTableVacancy()

                // continue polling after that
                this.interval = setInterval(() => {
                    this.fetchTableVacancy()
                }, 5000);
            }

        },
        
        fetchTableVacancy() {
            let r = this.$axios.get(API.BASE + API.TABLEVISION).then((apiResponse) => {
                var data = apiResponse.data
                
                this.tables = data.tables
                this.tableVisionAPIStatus = "LIVE"
            }).catch((error) => {
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
        }
    }
}
</script>