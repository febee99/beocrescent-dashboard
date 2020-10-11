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
        </b-tabs>

    </section>
</template>

<script>
import Overview from '@/pages/main'
import Nanyuan from '@/pages/nanyuan'
export default {

    head() {
        return {
            title: this.title,
        }
    },

    components: {
        Overview,
        Nanyuan
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
                this.triggerNYAPI()
            } else {
                this.$refs.nanyuan.startTableVisionAPIPolling(false)
            }
        }
    },

    methods: {
        triggerNYAPI() {
            // triggers the api polling once clicked
            this.$refs.nanyuan.startTableVisionAPIPolling(true)
        }
    }
}
</script>