<template>
  <div>
    <div
      class="tile is-child notification px-5"
      :style="{'background-color': color}"
    >
      <p class="is-size-4 has-text-weight-bold">{{idx}}번째 건의사항</p>
      {{ text }}

    </div>
  </div>
</template>
<script>
export default {
  props: {
    idx: Number,
    text: String,
    color: String,
  },
};
</script>
