<script>
import { Pie } from "vue-chartjs";

export default {
  extends: Pie,
  props: ["chartData", "options"],
  methods: {},
  mounted() {
    this.renderChart(this.chartData, this.options);
  },
};
</script>
