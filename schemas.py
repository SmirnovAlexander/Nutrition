from typing import List

from pydantic import BaseModel, field_validator


class Unit(BaseModel):
    name: str
    value: str


class Nutrient(BaseModel):
    name: str
    amount: str | None
    dvp: str | None
    # childNutrients: List[Nutrient] | None


class MetaNutrient(BaseModel):
    mainNutrient: Nutrient | None
    childNutrients: List[Nutrient] | None


class KeyNutrients(BaseModel):
    values: List[MetaNutrient]


class NutritionFacts(BaseModel):
    calorieInfo: MetaNutrient
    keyNutrients: KeyNutrients
    vitaminMinerals: MetaNutrient


class Idml(BaseModel):
    directions: List[Unit]
    indications: List[Unit] | None
    specifications: List[Unit]
    nutritionFacts: NutritionFacts


class Price(BaseModel):
    price: float
    priceString: str


class PriceInfo(BaseModel):
    currentPrice: Price
    unitPrice: Price


class Review(BaseModel):
    rating: float
    reviewText: str


class Reviews(BaseModel):
    averageOverallRating: float
    customerReviews: List[Review]
    totalReviewCount: int


class Item(BaseModel):
    name: str
    brand: str
    shortDescription: str
    canonicalUrl: str
    availabilityStatus: str
    averageRating: float
    priceInfo: PriceInfo
    idml: Idml
    reviews: Reviews

    @field_validator("canonicalUrl")
    def convert_url(cls, url):
        return "https://www.walmart.com" + url
