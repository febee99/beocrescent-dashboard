<template>
    <section class="section">
        <b-tabs position="is-centered" size="is-medium" class="block" v-model="activeTab">
            <b-tab-item label="Overview" icon="information-variant">
                <Overview/>
            </b-tab-item>
            <b-tab-item label="Nan Yuan Fishball" icon="noodles">
                <!-- nanyuan.vue -->
                <Nanyuan ref="nanyuan"/>
            </b-tab-item>
            <b-tab-item label="Hai Chee Fish Soup" icon="rice">
                <!-- haichee.vue -->
                <Haichee ref="haichee"/>
            </b-tab-item>
            <b-tab-item label="Soon Heng Lor Mee" icon="silverware-variant">
                <!-- soonheng.vue -->
                <SoonHeng ref="soonheng"/>
            </b-tab-item>
        </b-tabs>

    </section>
</template>

<script>
import Overview from '@/pages/main'
import Nanyuan from '@/pages/nanyuan'
import Haichee from '@/pages/haichee'
import SoonHeng from '@/pages/soonheng'
export default {

    head() {
        return {
            title: this.title,
        }
    },

    components: {
        Overview,
        Nanyuan,
        Haichee,
        SoonHeng
    },

    data() {
        return {
            title: 'Beo Crescent IoT Dashboard',
            activeTab: 0,
        }
    },

    watch: {
        activeTab: function() {
          if (this.activeTab == 1) {
              // Nanyuan Fishball Stall
              this.triggerNYAPI()
              this.$refs.haichee.startTableVisionAPIPolling(false)
              this.$refs.soonheng.startTableVisionAPIPolling(false)
          } else if (this.activeTab == 2){
              // Haichee Fish Soup
              this.triggerHCAPI()
              this.$refs.nanyuan.startTableVisionAPIPolling(false)
              this.$refs.soonheng.startTableVisionAPIPolling(false)
          } else if (this.activeTab == 3){
              // Soon Heng Lor Mee
              this.triggerSHAPI()
              this.$refs.nanyuan.startTableVisionAPIPolling(false)
              this.$refs.haichee.startTableVisionAPIPolling(false)
          } else {
              this.$refs.nanyuan.startTableVisionAPIPolling(false)
              this.$refs.haichee.startTableVisionAPIPolling(false)
              this.$refs.soonheng.startTableVisionAPIPolling(false)
          }
        }
    },

    methods: {
        triggerNYAPI() {
            // triggers the api polling once clicked
            this.$refs.nanyuan.startTableVisionAPIPolling(true)
        },
        triggerHCAPI() {
            // triggers the api polling once clicked
            this.$refs.haichee.startTableVisionAPIPolling(true)
        },
        triggerSHAPI() {
            // triggers the api polling once clicked
            this.$refs.soonheng.startTableVisionAPIPolling(true)
        }
    }
}
</script>
