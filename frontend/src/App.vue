<template>
  <div id="app">
    <search-form @submit="handleSearch" @show-modal="showModal = true" />
    <trip-details :fastestTrip="fastestTrip" :cheapestTrip="cheapestTrip" />
    <modal-warning v-if="showModal" @close="showModal = false" />
  </div>
</template>

<script>
import SearchForm from './components/SearchForm.vue';
import TripDetails from './components/TripDetails.vue';
import ModalWarning from './components/ModalWarning.vue';
import axios from 'axios';

export default {
  components: {
    SearchForm,
    TripDetails,
    ModalWarning
  },
  data() {
    return {
      fastestTrip: null,
      cheapestTrip: null,
      showModal: false
    };
  },
  methods: {
    async handleSearch(formData) {
      try {
        const response = await axios.get('http://localhost:3000/trips');
        const filterTrips= response.data.transport.filter((city)=>city == SearchForm)
        const trips = filterTrips.map((duration)=>duration.duration.slice(0,-1));
        console.log(trips);
        //response.data.transport.map((name)=>name.city)
        // Encontrar a viagem mais rápida
        let fastestTrip = trips.reduce((prev, curr) => {
          return parseFloat(curr.duration) < parseFloat(prev.duration) ? curr : prev;
        });

        // Encontrar a viagem mais econômica
        let cheapestTrip = trips.reduce((prev, curr) => {
          return parseFloat(curr.price_econ) < parseFloat(prev.price_econ) ? curr : prev;
        });

        // Atualizar o estado do componente com os detalhes das viagens
        this.fastestTrip = fastestTrip;
        this.cheapestTrip = cheapestTrip;
      } catch (error) {
        console.error('Erro ao buscar viagens:', error);
      }
    }
  }
};

</script>

<style>
#app {
  font-family: Arial, sans-serif;
  text-align: center;
  margin-top: 20px;
}
</style>
