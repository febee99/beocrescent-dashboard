<template>
    <div class="columns is-vcentered is-multiline">
        <div class="column is-4">
            <card-widget
                class="tile is-child"
                type="is-success"
                icon="account-multiple"
                :number="51"
                suffix="%"
                label="Positive tray return rate"
                description="Percentage of confirmed self-initiated tray returns"
            />
        </div>
        <div class="column is-4">
            <card-widget
                class="tile is-child"
                type="is-danger"
                icon="account-multiple"
                :number="86"
                suffix="%"
                label="Negative tray return rate"
                description="Unreturned trays or trays cleared by cleaners"
            />
        </div>
        <div class="column is-4">
            <card-widget
                class="tile is-child"
                type="is-info"
                icon="clock"
                :number="12"
                suffix="pm"
                label="Hour trays returned most"
                description="The 1-hour time period when trays are self-returned most"
            />
        </div>
        <div class="column is-6">
            <div class="card">
                <div class="card-content">
                    <p class="title">Some pie chart</p>
                    <doughnut-chart :chartData="this.trayReturnInsights"/>
                </div>
            </div>
        </div>
        <div class="column is-6">
            <div class="card">
                <div class="card-content">
                    <p class="title">Tray return chart</p>
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
export default {

    components: {
        CardWidget,
        DoughnutChart
    },

    data() {
        return {
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