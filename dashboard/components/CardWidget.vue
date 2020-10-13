<template>
    <card-component>
        <div class="level">
            <div class="level-item">
                <div class="is-widget-label">
                    <h3 class="subtitle is-spaced is-size-6-touch">
                        {{ label }}
                        <b-tooltip :label="description"
                            type="is-light"
                            position="is-top"
                            :active="active">
                            <sup><b-icon icon="help-circle-outline" size="is-small" type="is-grey" /></sup>
                        </b-tooltip>
                    </h3>
                    <h1 class="title is-size-5-touch">
                        <growing-number :value="number" :prefix="prefix" :suffix="suffix" />
                    </h1>
                </div>

            <div v-if="icon" class="level-item has-widget-icon">
                <div class="is-widget-icon">
                    <b-icon :icon="icon" size="is-large" :type="type" />
                </div>
            </div>
            </div>
        </div>
    </card-component>
</template>

<script>
import CardComponent from '@/components/CardComponent'
import GrowingNumber from '@/components/GrowingNumber'
export default {
    name: 'CardWidget',
    components: { GrowingNumber, CardComponent },
    props: {
        description: {
            type: String,
            default: "",
        },
        icon: {
            type: String,
            default: null,
        },
        number: {
            type: Number,
            default: 0,
        },
        prefix: {
            type: String,
            default: null,
        },
        suffix: {
            type: String,
            default: null,
        },
        label: {
            type: String,
            default: null,
        },
        type: {
            type: String,
            default: null,
        },
    },
}
</script>
