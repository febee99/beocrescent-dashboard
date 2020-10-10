<script>
import { Line } from 'vue-chartjs'

export default {
    extends: Line,
    props:['chartData','options'],
    methods: {
    },
    mounted () {
        this.renderChart(this.chartData, this.options)
    }
};
</script>
