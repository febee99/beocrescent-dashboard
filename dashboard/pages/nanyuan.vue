<template>
  <section>
    <p class="title m-5 pt-5">RFID-FSR-Motion Sensor Tray In/Out Data</p>
    <small class="subtitle has-text-grey m-5">Tray out from stall, tray in by cleaners. This helps to detect cleaner-returns.</small>
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
              ref="nanyuanLineChart"
              :chartData="this.cleanerReturnInsights"
            />
          </div>
        </div>
      </div>
      <div class="column is-4 has-text-centered">
        <div class="card">
          <div class="card-content">
            <p class="title is-size-5-touch">Tray Return Visualisation</p>
            <pie-chart ref="nanyuanPieChart" :chartData="this.nanyuanReturns" />
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
              suffix="%"
              label="Self-returns rate"
              description="Percentage of patrons who cleaned up their tables after eating today"
            />

            <card-widget
              class="tile is-child"
              type="is-danger"
              icon="account-multiple-minus"
              :number="this.cleanerReturn"
              suffix="%"
              label="Cleaner Return rate"
              description="Percentage of patrons who left their receptacles to the cleaners today"
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
        return "2020-10-12";
      } else {
        return (
          this.date.getFullYear() +
          "-" +
          (parseInt(this.date.getMonth()) + 1) +
          "-" +
          this.date.getDate()
        );
      }
    },
  },
  data() {
    var today = new Date();
    console.log("today is :" + today);
    return {
      rfidFsrAPIStatus: "Offline",
      rfidTrayInStatus: "Offline",
      rfidTrayIn: [],
      rfidFsrTable: [],
      TrayIn: [],
      loaded: false,
      rfid_loaded: false,
      interval: null,
      cleanerReturn: 0,
      selfReturn: 0,
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
      nanyuanReturns: {
        labels: ["Patrons Return Count", "Cleaner Return Count"],
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
      cleanerReturnInsights: {
        labels: [
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
            label: "Tray OUT",
            BackgroundColor: "white",
            borderWidth: 3,
            borderColor: "#ef4250",
            pointBorderColor: "#249EBF",
            data: [],
          },
          {
            label: "Tray IN",
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
    rfidFsrTable: function () {
      this.$refs.nanyuanLineChart.renderChart(this.cleanerReturnInsights);
    },

    rfidTrayIn: function () {
      this.$refs.nanyuanPieChart.renderChart(this.nanyuanReturns);
    },

    date: function () {
      this.getFsrRfidData();
      this.getRfidTrayIn();
    },
  },

  methods: {
    startAPIPolling(start) {
      // call fetch for the first time
      if (!start) {
        clearInterval(this.interval);
      } else {
        this.getFsrRfidData();
        this.getRfidTrayIn();
      }
    },
    getFsrRfidData() {
      // if (!this.loaded) {
      // this.loaded = true;
      this.cleanerReturnInsights.datasets[0].data = [];
      this.cleanerReturnInsights.datasets[1].data = [];
      let r = this.$axios
        .get(API.BASE + API.RFIDFSRVISIO)
        .then((apiResponse) => {
          var data = apiResponse.data;
          var date = this.selectedDate;
          console.log(date)
          var time_sensor_data = data[date];
          // console.log(date);
          console.log(Object.keys(time_sensor_data));
          for (var time of Object.keys(time_sensor_data)) {
            console.log(time);
            var data1 = time_sensor_data[time];
            this.rfidFsrTable.push(data1);
            this.cleanerReturnInsights.datasets[0].data.push(data1);
          }

          this.rfidFsrAPIStatus = "LIVE";
        });
      let t = this.$axios
        .get(API.BASE + API.RFIDTRAYIN)
        .then((apiResponse) => {
          var data = apiResponse.data;
          console.log(data);
          var date = this.selectedDate;
          var time_sensor_data = data[date];
          console.log(this.selectedDate);
          console.log(Object.keys(time_sensor_data));
          for (var time of Object.keys(time_sensor_data)) {
            console.log(time);
            var data1 = time_sensor_data[time];
            this.TrayIn.push(data1);
            console.log("HELLO");
            console.log(this.TrayIn);
            this.cleanerReturnInsights.datasets[1].data.push(data1);
          }
          this.rfidFsrAPIStatus = "LIVE";
        })
        .catch((error) => {
          this.rfidFsrAPIStatus = "Offline";
          this.rfidFsrTable = [];
          if (error.response != undefined) {
            var response = error.response.data;
            this.toastAlert(response.message, "is-danger", 5000);
            console.log("nanyuan " + response.message);
          } else {
            if (this.rfidFsrAPIStatus != "Offline") {
              this.toastAlert(error, "is-danger", 5000);
              console.log("nanyuan " + error);
            }
          }
        });
      // }
    },

    getRfidTrayIn() {
      // this.rfid_loaded = true;
      console.log(API.RFIDTRAYINOUT);
      // this.nanyuanReturns.datasets[0].data = [1, 1];
      let r = this.$axios
        .get(API.BASE + API.RFIDTRAYINOUT)
        .then((apiResponse) => {
          var data = apiResponse.data;

          var tray_in = data["CleanerReturn"];
          var self_return = data["SelfReturn"];
          console.log(tray_in)
          console.log(self_return)
          var total = self_return + tray_in;

          this.cleanerReturn = parseFloat((tray_in / total) * 100).toFixed(2);
          this.selfReturn = parseFloat((self_return / total) * 100).toFixed(2);

          var data1 = [tray_in, self_return];
          // console.log(this.nanyuanReturns.datasets[0].data);
          this.nanyuanReturns.datasets[0].data = [self_return, tray_in];
          // console.log(this.nanyuanReturns.datasets[0].data);
          // this.$ref.nanyuanPieChart.updateChart();
          // this.$ref.nanyuanPieChart.renderChart(this.nanyuanReturns);
          this.rfidTrayIn.push(0);

          // this.nanyuanReturns.datasets[0].data.push(tray_in);

          this.rfidFsrAPIStatus = "LIVE";
        })
        .catch((error) => {
          this.rfidTrayInStatus = "Offline";
          this.getRfidTrayIn1 = [];
          if (error.response != undefined) {
            var response = error.response.data;
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
