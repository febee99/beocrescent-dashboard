<template>
  <section>
    <p class="title m-5 pt-5">Weight & Infrared sensor tray-returns data</p>
    <div></div>
    <div class="columns mt-5 is-multiline is-tablet">
      <div class="column is-4 has-text-centered">
        <div class="card">
          <div class="card-content">
            <p class="title is-size-5-touch">Daily Tray Return Count</p>
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
              ref="haichewLineChart"
              :chartData="this.patronReturnInsights"
            />
          </div>
        </div>
      </div>
      <div class="column is-4 has-text-centered">
        <div class="card">
          <div class="card-content">
            <p class="title is-size-5-touch">Tray Return Visualisation</p>
            <pie-chart ref="haichewPieChart" :chartData="this.haichewReturns" />
          </div>
        </div>
      </div>
      <div class="column is-4 has-text-centered">
        <div class="card">
          <div class="card-content">
            <p class="title is-size-5-touch">Tray Return Rate</p>
            <card-widget
              class="tile is-child"
              type="is-success"
              icon="charity"
              :number="this.selfReturn"
              :key="selfReturn"
              suffix="%"
              label="At this station"
              description="Percentage of patrons who returned their trays to this tray return point"
            />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import CardWidget from "@/components/CardWidget";
import CardComponent from "@/components/CardComponent";
import LineChart from "@/components/LineChart";
import API from "@/constants/api";
import PieChart from "@/components/PieChart";

export default {
  components: {
    CardWidget,
    CardComponent,
  },
  computed: {
    selectedDate: function () {
      if (!this.date) {
        console.log("Not this.date");
        return "2020-10-12";
      } else {
        //console.log(this.date);
        return (
          this.date.getFullYear() +
          "-" +
          (parseInt(this.date.getMonth()) + 1) +
          "-" +
          this.date.getDate()
        );
      }
    }
  },
  data() {
    var today = new Date();
    return {
      date: today,
      minDate: new Date(
        today.getFullYear() - 80,
        today.getMonth(),
        today.getDate()
      ),
      maxDate: new Date(
        today.getFullYear(),
        today.getMonth(),
        today.getDate()
      ),

      lineChartAPIStatus: "Offline",
      lineChartTable: [],
      interval: null,

      pieChartAPIStatus: "Offline",
      pieChartTable: [],

      selfReturn: 0,

      haichewReturns: {
        labels: ["Trays Returned Here", "Trays Not Returned Here"],
        datasets: [
          {
            backgroundColor: ["#ee4350", "#409cd2"],
            pointBackgroundColor: "white",
            borderWidth: 1,
            pointBorderColor: "#249EBF",
            data: [],
          },
        ],
      },
      patronReturnInsights: {
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
            label: "Tray distributed",
            BackgroundColor: "white",
            borderWidth: 3,
            borderColor: "#ef4250",
            pointBorderColor: "#249EBF",
            data: [],
          },
          {
            label: "Trays returned",
            BackgroundColor: "#white",
            borderWidth: 3,
            borderColor: "#7AD7F0",
            pointBorderColor: "#7AD7F0",
            data: [],
          },
        ],
      },
    };
  },

  watch: {
    lineChartTable: function () {
      this.$refs.haichewLineChart.renderChart(this.patronReturnInsights);
    },

    pieChartTable: function () {

      this.$refs.haichewPieChart.renderChart(this.haichewReturns);

    },

    date: function () {
      this.patronReturnInsights.datasets[0].data =[];
      this.patronReturnInsights.datasets[1].data = [];
      this.getLineChartData();
      this.getPieChartData();
    }
  },

  methods: {
    startAPIPolling(start) {
      // call fetch for the first time
      if (!start) {
        clearInterval(this.interval);
      } else {
        this.getPieChartData();
        this.getLineChartData();

      }
    },
    getLineChartData() {

      let trays_distributed = this.$axios
        .get(API.BASE + API.DISTRVISION + "/1/" + this.selectedDate )
        .then((apiResponse) => {
          var data = apiResponse.data;
          //console.log(Object.keys(time_sensor_data));
          for (var time of Object.keys(data)) {
            //console.log(time);
            var data1 = data[time];
            this.lineChartTable.push(data1);
            this.patronReturnInsights.datasets[0].data.push(data1);
          }

          this.lineChartAPIStatus = "LIVE";
        });

      let trays_returned = this.$axios
        .get(API.BASE + API.RETURNVISION + "/1/" + this.selectedDate )
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
            console.log("nanyuan " + response.message);
          } else {
            if (this.lineChartAPIStatus != "Offline") {
              this.toastAlert(error, "is-danger", 5000);
              console.log("nanyuan " + error);
            }
          }
        });

    },

    getPieChartData() {

      let r = this.$axios
        .get(API.BASE + API.STALLTOTALVISION + "/1/" + this.selectedDate)
        .then((apiResponse) => {
          var data = apiResponse.data;

          var not_returned = data["NotReturned"];
          var returned = data["Returned"];

          var total = not_returned + returned;
          console.log("Total: " + total);
          console.log("Returned:" + returned);

          this.selfReturn = parseFloat((returned / total) * 100).toFixed(0);
          console.log(this.selfReturn);
          var data1 = [not_returned, returned];
          this.haichewReturns.datasets[0].data = [returned, not_returned];
          this.pieChartTable.push(0);
          this.rfidFsrAPIStatus = "LIVE";
        })
        .catch((error) => {
          this.pieChartAPIStatus = "Offline";
          if (error.response != undefined) {
            var response = error.response.data;
            this.pieChartTable = [];
            this.toastAlert(response.message, "is-danger", 5000);
            console.log("nanyuan " + response.message);
          } else {
            if (this.rfidFsrAPIStatus != "Offline") {
              this.toastAlert(error, "is-danger", 5000);
              console.log("nanyuan " + error);
            }
          }
        });
    },
  },
};
</script>
