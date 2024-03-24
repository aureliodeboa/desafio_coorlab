<template>
  <div>
    <h2>Trip Details</h2>
    <div v-if="fastestTrip">
      <p>Fastest Trip:</p>
      <p>Company: {{ fastestTrip.name }}</p>
      <p>Duration: {{ fastestTrip.duration }}</p>
      <p>Price: {{ fastestTrip.price_confort }}</p>
    </div>
    <div v-if="cheapestTrip">
      <p>Cheapest Trip:</p>
      <p>Company: {{ cheapestTrip.name }}</p>
      <p>Duration: {{ cheapestTrip.duration }}</p>
      <p>Price: {{ cheapestTrip.price_econ }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    fastestTrip: Object,
    cheapestTrip: Object
  }
};
</script>
