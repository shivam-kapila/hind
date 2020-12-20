// import APIError from "./APIError";

export default class APIService {
  APIBaseURI: string;

  constructor(APIBaseURI: string) {
    let finalUri = APIBaseURI;
    if (finalUri.endsWith("/")) {
      finalUri = finalUri.substring(0, APIBaseURI.length - 1);
    }
    this.APIBaseURI = finalUri;
  }
}
