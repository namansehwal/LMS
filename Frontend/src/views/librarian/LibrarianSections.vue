<template>
    <div class="container mt-5">
      <h2>Sections</h2>
  
      <!-- Add Section Form -->
      <div class="card mt-4">
        <div class="card-header">
          Add Section
        </div>
        <div class="card-body">
          <form @submit.prevent="addSection">
            <div class="mb-3">
              <label for="sectionName" class="form-label">Section Name</label>
              <input v-model="newSection.name" type="text" class="form-control" id="sectionName" required>
            </div>
            <div class="mb-3">
              <label for="description" class="form-label">Description</label>
              <textarea v-model="newSection.description" class="form-control" id="description" rows="3" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Add Section</button>
          </form>
        </div>
      </div>
  
      <!-- Display Sections -->
      <div class="card mt-4">
        <div class="card-header">
          All Sections
        </div>
        <div class="card-body">
          <table class="table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Description</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="section in sections" :key="section.id">
                <td>{{ section.id }}</td>
                <td>{{ section.name }}</td>
                <td>{{ section.description }}</td>
                <td>
                  <button @click="editSection(section)" class="btn btn-warning btn-sm">Edit</button>
                  <button @click="deleteSection(section.id)" class="btn btn-danger btn-sm">Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
  
      <!-- Edit Section Form -->
      <div v-if="editingSection" class="card mt-4">
        <div class="card-header">
          Edit Section
        </div>
        <div class="card-body">
          <form @submit.prevent="updateSection">
            <div class="mb-3">
              <label for="editSectionName" class="form-label">Section Name</label>
              <input v-model="editingSection.name" type="text" class="form-control" id="editSectionName" required>
            </div>
            <div class="mb-3">
              <label for="editDescription" class="form-label">Description</label>
              <textarea v-model="editingSection.description" class="form-control" id="editDescription" rows="3" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Update Section</button>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        newSection: {
          name: '',
          description: ''
        },
        sections: [],
        editingSection: null
      };
    },
    mounted() {
      this.getAllSections();
    },
    methods: {
      async addSection() {
        try {
          const response = await this.$axios.post('/section', this.newSection);
          this.getAllSections();
          // Clear the form after adding the section
          this.newSection = {
            name: '',
            description: ''
          };
        } catch (error) {
          console.error('Add Section failed:', error);
        }
      },
      async getAllSections() {
        try {
          const response = await this.$axios.get('/section');
          this.sections = response.data;
        } catch (error) {
          console.error('Get Sections failed:', error);
        }
      },
      editSection(section) {
        this.editingSection = { ...section };
      },
      async updateSection() {
        try {
          await this.$axios.put(`/section`, {
            id: this.editingSection.id,
            name: this.editingSection.name,
            description: this.editingSection.description
          });
          
          this.editingSection = null;
          this.getAllSections();
        } catch (error) {
          console.error('Update Section failed:', error);
        }
      },
      async deleteSection(sectionId) {
        try {
          await this.$axios.delete(`/section`, { data: { id: sectionId } });
          this.getAllSections();
        } catch (error) {
          console.error('Delete Section failed:', error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add custom styles if needed */
  </style>
  