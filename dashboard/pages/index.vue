<template>
    <section class="section">
        <b-tabs position="is-centered" size="is-medium" class="block">
            <b-tab-item label="Overview" icon="information-variant">
                <Overview/>
            </b-tab-item>
            <b-tab-item label="Nan Yuan Fishball" icon="noodles">
                <!-- nanyuan.vue -->
                <Nanyuan/>
            </b-tab-item>
        </b-tabs>

    </section>
</template>

<script>
import Overview from '@/pages/main'
import Nanyuan from '@/pages/nanyuan'
export default {
    name: 'Beo Crescent Dashboard',

    components: {
        Overview,
        Nanyuan
    },

    data() {
        return {
        }
    }
}
</script>