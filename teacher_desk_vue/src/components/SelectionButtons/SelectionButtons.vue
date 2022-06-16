<template>
  <div class="column">
    <div class="tile is-ancestor">
      <slot></slot>
      <div
        class="tile is-parent"
        v-for="(button_info, index) in button_infos"
        :key="index"
      >
        <button
          :class="[defaultClass, {'is-info':selected_data==button_info.value, 'has-background-grey':selected_data!=button_info.value}]"
          @click="$emit('buttonSeletedEvent', button_info.value)"
        >
          {{ button_info.name }}
        </button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      defaultClass:
        "button is-fullwidth is-fullheight has-text-white is-size-4-desktop is-size-4-tablet is-size-5-mobile has-text-weight-bold",
    };
  },
  computed: {
    classObject() {
      return { "is-info": true };
    },
  },
  emits: ["buttonSeletedEvent"],
  props: {
    button_infos: Array,
    selected_data: [String, Boolean],
  },
};
</script>

<style scoped>
.button {
  border-radius: 20px;
}
</style>