import React from 'react'
import "./app.css"

import { Artice, Brand, CTA, Feature, Navbar } from "./components"
import { Blog, Features, Footer, Header, Possibility, WhatGPT3 } from "./containers"

const App = () => {
    return (
        <div className='app'>
            <Navbar />
            <Header />
            <Brand />
            <WhatGPT3 />
            <Features />
            <Feature />
            <Possibility />
            <Blog />
            <Artice />
            <CTA />
            <Footer />
        </div>
    )
}

export default App