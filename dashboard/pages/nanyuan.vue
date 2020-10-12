<template>
  <section>
    <p class="title m-5 pt-5">RFID-tagged tray-returns data</p>
    <!-- <div>
      <label for="example-datepicker">Choose a date</label>
      <b-form-datepicker
        id="example-datepicker"
        v-model="value"
        class="mb-2"
      ></b-form-datepicker>
      <p>Value: '{{ value }}'</p>
    </div> -->
    <div class="columns mt-5 is-vcentered is-multiline">
      <div class="column is-4 has-text-centered">
        <div class="card">
          <div class="card-content">
            <p class="title">Daily Tray Return Count</p>
            <line-chart ref="nanyuanLineChart" :chartData="this.cleanerReturnInsights" />
          </div>
        </div>
      </div>
      <div class="column is-4 has-text-centered">
        <div class="card">
          <div class="card-content">
            <p class="title">Tray Return Count</p>
            <pie-chart ref="nanyuanPieChart" :chartData="this.nanyuanReturns" />
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
    <br />
    <hr />
    <br />
    <p class="title m-5 pt-5">Tablevision data</p>
    <div class="columns mt-5 is-vcentered is-multiline">
      <div class="column is-4 has-text-centered">
        <div class="card">
          <div class="card-content">
            <p class="title">Table occupancy</p>
            <p class="has-text-weight-bold">
              API Status:
              <span
                :class="
                  tableVisionAPIStatus == 'LIVE'
                    ? 'has-text-success'
                    : 'has-text-danger'
                "
                >{{ this.tableVisionAPIStatus }}</span
              >
            </p>
            <b-tag
              :type="
                leTable.state == 0
                  ? 'is-success'
                  : leTable.state == 1
                  ? 'is-warning'
                  : 'is-danger'
              "
              class="my-2"
              size="is-large"
              :id="leTable.table"
              v-for="leTable in tables"
              v-bind:key="leTable.table"
            >
              <p>{{ leTable.table }}</p>
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
      </div>
      <div class="column is-4">
        <card-widget
          class="tile is-child"
          type="is-info"
          icon="charity"
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
          icon="silverware-clean"
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
import CardWidget from "@/components/CardWidget";
import CardComponent from "@/components/CardComponent";
import LineChart from "@/components/LineChart";
import PieChart from "@/components/PieChart";
import API from "@/constants/api";
// import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
// Vue.use(BootstrapVue);
// import "bootstrap/dist/css/bootstrap.css";
// import "bootstrap-vue/dist/bootstrap-vue.css";
// import "./custom.scss";

export default {
  components: {
    CardWidget,
    CardComponent,
  },

  data() {
    return {
      tableVisionAPIStatus: "Offline",
      rfidFsrAPIStatus: "Offline",
      rfidTrayInStatus: "Offline",
      tables: [],
      rfidTrayIn: [],
      rfidFsrTable: [],
      TrayIn: [],
      loaded: false,
      rfid_loaded:false,
      interval: null,

      nanyuanReturns: {
        labels: [
          "Patrons Return Count",
          "Cleaner Return Count",
        ],
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
    rfidFsrTable: function() {
      this.$refs.nanyuanLineChart.renderChart(this.cleanerReturnInsights)
    },

    rfidTrayIn: function() {
      this.$ref.nanyuanPieChart.renderChart(this.nanyuanReturns)
    }


  },

  methods: {
    startTableVisionAPIPolling(start) {
      // call fetch for the first time
      if (!start) {
        clearInterval(this.interval);
      } else {
        // this.fetchTableVacancy();
        this.get_fsr_rfid_data();
        this.get_rfidTrayIn();

        // continue polling after that
        this.interval = setInterval(() => {
        //   this.fetchTableVacancy();
          this.get_fsr_rfid_data();
          // this.get_rfidTrayIn();
        }, 5000);
      }
    },
    fetchTableVacancy() {
      let r = this.$axios
        .get(API.BASE + API.TABLEVISION)
        .then((apiResponse) => {
          var data = apiResponse.data;

          this.tables = data.tables;
          this.tableVisionAPIStatus = "LIVE";
        })
        .catch((error) => {
          this.tableVisionAPIStatus = "Offline";
          this.tables = [];
          if (error.response != undefined) {
            var response = error.response.data;
            this.toastAlert(response.message, "is-danger", 5000);
            console.log("table vision " + response.message);
          } else {
            if (this.tableVisionAPIStatus != "Offline") {
              this.toastAlert(error, "is-danger", 5000);
              console.log("table vision " + error);
            }
          }
        });
    },
    get_fsr_rfid_data() {
      if (!this.loaded) {
        this.loaded = true;
        let r = this.$axios
          .get(API.BASE + API.RFIDFSRVISIO)
          .then((apiResponse) => {
            var data = apiResponse.data;
            var date = "2020-10-12";
            var time_sensor_data = data[date];
            // console.log(date);
            console.log(Object.keys(time_sensor_data));
            for (var time of Object.keys(time_sensor_data)) {
              console.log(time);
              var data1 = time_sensor_data[time];
              this.rfidFsrTable.push(data1);
              this.cleanerReturnInsights.datasets[0].data.push(data1)
            }

            this.rfidFsrAPIStatus = "LIVE";
          })
        let t = this.$axios
          .get(API.BASE + API.RFIDTRAYIN)
          .then((apiResponse) => {
            var data = apiResponse.data;
            console.log(data)
            var date = "2020-10-12";
            var time_sensor_data = data[date];
            // console.log(date);
            console.log(Object.keys(time_sensor_data));
            for (var time of Object.keys(time_sensor_data)) {
              console.log(time);
              var data1 = time_sensor_data[time];
              this.TrayIn.push(data1);
              console.log("HELLO")
              console.log(this.TrayIn)
              this.cleanerReturnInsights.datasets[1].data.push(data1)
            }
            this.rfidFsrAPIStatus = "LIVE";
          })
          .catch((error) => {
            this.rfidFsrAPIStatus = "Offline";
            this.rfidFsrTable = [];
            if (error.response != undefined) {
              var response = error.response.data;
              this.toastAlert(response.message, "is-danger", 5000);
              console.log("table vision " + response.message);
            } else {
              if (this.rfidFsrAPIStatus != "Offline") {
                this.toastAlert(error, "is-danger", 5000);
                console.log("table vision " + error);
              }
            }
          });
      }
    },


    get_rfidTrayIn() {

        this.rfid_loaded = true
        console.log(API.RFIDTRAYINOUT)
        let r = this.$axios
          .get(API.BASE + API.RFIDTRAYINOUT)
          .then((apiResponse) => {
            var data = apiResponse.data;

            var tray_in = data["CleanerReturn"]
            var self_return = data["SelfReturn"]
            var data1 = [tray_in, self_return]

            this.nanyuanReturns.datasets[0].data.push(self_return)
            this.nanyuanReturns.datasets[0].data.push(tray_in)

            this.rfidFsrAPIStatus = "LIVE";
          })
          .catch((error) => {
            this.rfidTrayInStatus = "Offline";
            this.get_rfidTrayIn = [];
            if (error.response != undefined) {
              var response = error.response.data;
              this.toastAlert(response.message, "is-danger", 5000);
              console.log("table vision " + response.message);
            } else {
              if (this.rfidFsrAPIStatus != "Offline") {
                this.toastAlert(error, "is-danger", 5000);
                console.log("table vision " + error);
              }
            }
          });

    },
  },
};
</script>
