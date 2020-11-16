<template>
  <section>
    <!-- <p class="title m-5 pt-5">Weight & Infrared sensor tray-returns data</p> -->
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
            <p class="title is-size-5-touch">Cleaner's Clearing Count</p>
            <card-widget
              class="tile is-child"
              type="is-info"
              icon="broom"
              :number="this.cleanerClear"
              :key="cleanerClear"
              label="At this station"
              description="Number of times cleaners have cleared the tray return point"
            />
          </div>
        </div>
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
        <div class="card">
          <div class="card-content">
            <bar-chart
              ref="haichewBarChart"
              :chartData="this.overallInsights"
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
import BarChart from "@/components/BarChart";
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
        console.log(this.date.getDate());
        return "2020,10,12";
      } else {
        // console.log(this.date);
        // console.log((this.date.getDate() + "").length);
        return (
          this.date.getFullYear() +
          "," +
          (parseInt(this.date.getMonth()) + 1) +
          "," +
          ((this.date.getDate() + "").length == 1 ? "0" + this.date.getDate() : this.date.getDate())
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
      interval: null,
      lineChartAPIStatus: "Offline",
      lineChartTable: [],
      pieChartAPIStatus: "Offline",
      pieChartTable: [],
      barChartAPIStatus: "Offline",
      barChartTable: [],
      selfReturn: 0,
      cleanerClear: 0,
      haichewReturns: {
        labels: ["Trays Returned Here", "Trays Not Returned Here"],
        datasets: [
          {
            backgroundColor: ["#409cd2", "#ee4350"],
            pointBackgroundColor: "white",
            borderWidth: 1,
            pointBorderColor: "#249EBF",
            data: [],
          },
        ],
      },
      overallInsights: {
        labels: ["19 Oct", "23 Oct", "26 Oct", "7 Nov"],
        datasets: [
          {
            label: "Trays returned",
            BackgroundColor: "#white",
            borderWidth: 3,
            borderColor: "#7AD7F0",
            pointBorderColor: "#7AD7F0",
            data: [],
            hidden: true,
          },
          {
            label: "Tray distributed",
            BackgroundColor: "white",
            borderWidth: 3,
            borderColor: "#ef4250",
            pointBorderColor: "#249EBF",
            data: [],
            hidden: true,
          },
          {
            label: "Tray return rate",
            BackgroundColor: "white",
            borderWidth: 3,
            borderColor: "#3BB143",
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
            label: "Trays returned",
            BackgroundColor: "#white",
            borderWidth: 3,
            borderColor: "#7AD7F0",
            pointBorderColor: "#7AD7F0",
            data: [],
          },
          {
            label: "Tray distributed",
            BackgroundColor: "white",
            borderWidth: 3,
            borderColor: "#ef4250",
            pointBorderColor: "#249EBF",
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

    barChartTable: function () {
      this.$refs.haichewBarChart.renderChart(this.overallInsights);
    },
    date: function () {
      this.haichewReturns.datasets[0].data = [];
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
        this.getLineChartData()
        this.getPieChartData()
        this.getBarChartData()

       
        this.interval = setInterval(() => {
                          this.patronReturnInsights.datasets[0].data =[];
                          this.patronReturnInsights.datasets[1].data =[];
                          this.getLineChartData()
                          this.getPieChartData()

                        }, 10000);
      }
    },
    getLineChartData() {
      
        let trays_returned = this.$axios
        .get(API.BASE + API.RETURNDISTRVISION + "/1/" + this.selectedDate )
        .then((apiResponse) => {
          var data = apiResponse.data;
          var returns = data["returns"]
          var distr = data["distr"]
          for (var time of Object.keys(returns)) {
            var data1 = returns[time];
            this.lineChartTable.push(data1);
            this.patronReturnInsights.datasets[0].data.push(data1);

        }
        for (var time of Object.keys(distr)) {
            var data1 = distr[time];
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
            console.log("haichew " + response.message);
          } else {
            if (this.lineChartAPIStatus != "Offline") {
              this.toastAlert(error, "is-danger", 5000);
              console.log("haichew " + error);
            }
          }
        });
    },

    getBarChartData() {
      
      let trays_returned = this.$axios
        .get(API.BASE + API.BARCHART)
        .then((apiResponse) => {
          var data = apiResponse.data;
          var returns = data["returns"]
          var distr = data["distr"]
          console.log(returns)
          console.log(distr)
          for (var key1 of Object.keys(returns)) {
            for (var key2 of Object.keys(distr)) {
              if (key1 == key2) {
                console.log(key1);
                console.log(returns[key1]);
                this.barChartTable.push(returns[key1]);
                this.overallInsights.datasets[0].data.push(returns[key1]);
                this.overallInsights.datasets[1].data.push(distr[key2]);
                this.overallInsights.datasets[2].data.push(parseFloat((returns[key1] / distr[key2] * 100)).toFixed(0));
              }
          }
        }
   

        this.barChartAPIStatus = "LIVE";
        })
        .catch((error) => {
          this.barChartAPIStatus = "Offline";
          this.barChartTable = [];
          if (error.response != undefined) {
            var response = error.response.data;
            this.toastAlert(response.message, "is-danger", 5000);
            console.log("haichew bar chart" + response.message);
          } else {
            if (this.barChartAPIStatus != "Offline") {
              this.toastAlert(error, "is-danger", 5000);
              console.log("haichew bar chart" + error);
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
          var cleared = data["Cleared"];
          var total = not_returned + returned;
          console.log("Total: " + total);
          console.log("Returned:" + returned);

          this.selfReturn = parseFloat((returned / total) * 100).toFixed(0);
          this.cleanerClear = cleared;
          console.log(this.selfReturn);
          var data1 = [not_returned, returned];
          this.haichewReturns.datasets[0].data = [returned, not_returned];
          this.pieChartTable.push(0);
          this.pieChartAPIStatus = "LIVE";
        })
        .catch((error) => {
          this.pieChartAPIStatus = "Offline";
          if (error.response != undefined) {
            var response = error.response.data;
            this.pieChartTable = [];
            this.toastAlert(response.message, "is-danger", 5000);
            console.log("haichew pie chart " + response.message);
          } else {
            if (this.pieChartAPIStatus != "Offline") {
              this.toastAlert(error, "is-danger", 5000);
              console.log("haichew pie chart" + error);
            }
          }
        });
    },
  },
};
</script>
