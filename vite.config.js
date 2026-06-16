import { defineConfig } from 'vite'
import { resolve } from 'path'
import { fileURLToPath } from 'url'
import { dirname } from 'path'

const __filename = fileURLToPath(import.meta.url)
const __dirname = dirname(__filename)

export default defineConfig({
  server: {
    port: parseInt(process.env.PORT) || 5173
  },
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        drivewayProjects: resolve(__dirname, 'driveway-projects.html'),
        walkwayProjects: resolve(__dirname, 'walkway-projects.html'),
        patioProjects: resolve(__dirname, 'patio-projects.html'),
        stepProjects: resolve(__dirname, 'step-projects.html'),
        stampedConcreteProjects: resolve(__dirname, 'stamped-concrete-projects.html'),
        commercialProjects: resolve(__dirname, 'commercial-projects.html'),
        fencingProjects: resolve(__dirname, 'fencing-projects.html'),
        deckProjects: resolve(__dirname, 'deck-projects.html'),
        outdoorStructureProjects: resolve(__dirname, 'outdoor-structure-projects.html'),
        testimonials: resolve(__dirname, 'testimonials.html'),
        serviceArea: resolve(__dirname, 'service-area.html'),
        contact: resolve(__dirname, 'contact.html'),
        highPoint: resolve(__dirname, 'high-point.html'),
        greensboro: resolve(__dirname, 'greensboro.html'),
        winstonSalem: resolve(__dirname, 'winston-salem.html'),
        kernersville: resolve(__dirname, 'kernersville.html'),
        thomasville: resolve(__dirname, 'thomasville.html'),
        oakRidge: resolve(__dirname, 'oak-ridge.html'),
        summerfield: resolve(__dirname, 'summerfield.html'),
        clemmons: resolve(__dirname, 'clemmons.html'),
        lexington: resolve(__dirname, 'lexington.html'),
        colfax: resolve(__dirname, 'colfax.html'),
        archdale: resolve(__dirname, 'archdale.html'),
        jamestown: resolve(__dirname, 'jamestown.html'),
        walkertown: resolve(__dirname, 'walkertown.html'),
        walburg: resolve(__dirname, 'walburg.html'),
        trinity: resolve(__dirname, 'trinity.html'),
        unionCross: resolve(__dirname, 'union-cross.html'),
        midway: resolve(__dirname, 'midway.html'),
        faqs: resolve(__dirname, 'faqs.html')
      }
    }
  }
})
