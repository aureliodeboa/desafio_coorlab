<template>
  <div>
    <label for="destination">Destination:</label>
    <select v-model="selectedDestination">
      <option v-for="city in cities" :value="city">{{ city }}</option>
    </select>
    <label for="date">Date:</label>
    <input type="date" id="date" v-model="date">
    <button @click="handleSubmit">Search</button>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      selectedDestination: '',
      date: '',
      cities: []
    };
  },
  created() {
    this.fetchCities();
  },
  methods: {
    async fetchCities() {
      try {
        const response = await axios.get('http://localhost:3000/trips');
        this.cities = response.data.transport.map((name)=>name.city);
      } catch (error) {
        console.error('Error fetching cities:', error);
      }
    },
    handleSubmit() {
      if (!this.selectedDestination || !this.date) {
        this.$emit('show-modal');
      } else {
        this.$emit('submit', {
          destination: this.selectedDestination,
          date: this.date
        });
      }
    }
  }
};
</script>
