class UriBuilder {
  constructor(url) {
    const [real, ...rest]=url.split("?")
    this.url=real
    this.params={}
    for (let p of rest) {
      const [key, val]=p.split("=")
      this.params[key]=val
    }
  }
  build() {
    let parameters=Object.entries(this.params).reduce((prev, cur) => {
      const [key, val]=cur
      return [...prev, `${key}=${val}`]
    }, [])
    return this.url+"?"+encodeURI(parameters.join("&"))
  }
}