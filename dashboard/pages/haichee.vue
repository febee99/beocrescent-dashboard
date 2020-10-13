<template>
  <section>
    <p class="title m-5 pt-5">Patrons tray-returns data</p>
    {{ this.rfidFsrTable }}
    <div class="columns mt-5 is-vcentered is-multiline">
      <div class="column is-4 has-text-centered">
        <div class="card">
          <div class="card-content">
            <line-chart ref="haicheeLineChart" :chartData="this.patronReturnInsights" />
          </div>
        </div>
      </div>
      <div class="column is-4 has-text-centered">
        <div class="card">
          <div class="card-content">
            <pie-chart :chartData="this.haicheeReturns" />
          </div>
        </div>
      </div>
      <div class="column is-4 has-text-centered">
        <div class="card">
          <div class="card-content">
            <p class="title">Data Analysis</p>
            <card-widget
              class="tile is-child"
              type="is-info"
              icon="clock"
              :number="12"
              suffix="pm"
              label="Hour trays returned most"
              description="The 1-hour time period when trays are self-returned most"
            />

            <card-widget
              class="tile is-child"
              type="is-info"
              icon="thumb-up"
              :number="84"
              suffix="%"
              label="Self-returns rate"
              description="Percentage of patrons who cleaned up their tables after eating today"
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
      tables: [],
      rfidFsrTable: [],
      loaded: false,

      interval: null,

      haicheeReturns: {
        labels: [
          "Trays not returned by patrons",
          "Trays returned by patrons",
        ],
        datasets: [
          {
            backgroundColor: ["#ee4350", "#409cd2"],
            pointBackgroundColor: "white",
            borderWidth: 1,
            pointBorderColor: "#249EBF",
            data: [60, 200],
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
            label: "Hai Chee Fish Soup Stall",
            pointBackgroundColor: "white",
            borderWidth: 3,
            pointBorderColor: "#249EBF",
            data: [],
          },
        ],
      },
    };
  },

  watch: {
    rfidFsrTable: function() {
        this.$refs.haicheeLineChart.renderChart(this.patronReturnInsights)
    }
  },

  methods: {
    startAPIPolling(start) {
      // call fetch for the first time
      if (!start) {
        clearInterval(this.interval);
      } else {
        // this.fetchTableVacancy();
        this.get_fsr_rfid_data();
        // continue polling after that
        this.interval = setInterval(() => {
        //   this.fetchTableVacancy();
          this.get_fsr_rfid_data();
        }, 5000);
      }
    },
    get_fsr_rfid_data() {
      if (!this.loaded) {
        this.loaded = true;
        let r = this.$axios
          .get(API.BASE + API.TRAYRETURNVISION)
          .then((apiResponse) => {
            var data = apiResponse.data;
            var date = "2020-10-12";
            // console.log(data);
            // this.  = [];
            var test = [];
            var time_sensor_data = data[date];
            // console.log(date);
            console.log(Object.keys(time_sensor_data));
            for (var time of Object.keys(time_sensor_data)) {
              console.log(time);
              var data1 = time_sensor_data[time];
              this.rfidFsrTable.push(data1);
              this.patronReturnInsights.datasets[0].data.push(data1)
              console.log(this.patronReturnInsights)
            }
            // this.rfidFsrTable = data.rfidFsrTable;
            console.log(test);
            // console.log(this.patronReturnInsights.datasets.data);

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
  },
};
</script>
