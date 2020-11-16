<template>
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
</template>

<script>
import CardWidget from '@/components/CardWidget'
import CardComponent from '@/components/CardComponent'
import DoughnutChart from '@/components/DoughnutChart'
import LineChart from '@/components/LineChart'
import PieChart from '@/components/PieChart'
import CardText from '@/components/CardTextComponent'
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
        }
    }
}
</script>