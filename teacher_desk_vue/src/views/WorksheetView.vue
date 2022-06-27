<template>
  <div class="section">
    <div class="columns is-variable is-8">
      <div class="column">
        <worksheet-tile></worksheet-tile>
      </div>
      <div class="column">
        <worksheet-tile></worksheet-tile>
      </div>
      <div class="column">
        <worksheet-tile></worksheet-tile>
      </div>

    </div>

  </div>
</template>
<script>
import WorksheetTile from "@/components/WorksheetTile.vue";
export default { components: { WorksheetTile } };
</script>
