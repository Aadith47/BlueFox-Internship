# 1.Convert ONLY ONE known bug to "solved" using the full dictionary path.

# school["campus"]["main_block"]["classrooms"]["grade_8"]["smart_board"]["status"] = "solved"

# food_app["modules"]["customer"]["cart"]["add_item"]["status"] = "solved"


# 2.Write a recursive function count_bugs(data)
# 3.Write a function solve_bugs(data) that converts every "bug" to "solved".


from icecream import ic

def replacing(data):
    
    for key, value in data.items():

        if isinstance(value, dict):
            replacing(value)

        elif value == "bug":
            data[key] = "solved"

def count_bugs(data):
    count = 0

    for key, value in data.items():

        if isinstance(value, dict):
            count += count_bugs(value)

        elif value == "bug":
            count += 1


    return count

def main():

    school = {
        "name": "Green Valley School",

        "campus": {
            "main_block": {
                "classrooms": {
                    "grade_8": {
                        "attendance_app": {
                            "status": "working"
                        },
                        "smart_board": {
                            "status": "bug"
                        }
                    },
                    "grade_10": {
                        "lab_booking": "working"
                    }
                },

                "library": {
                    "issue_book": {
                        "status": "bug",
                        "priority": "medium"
                    },
                    "return_book": {
                        "status": "working"
                    }
                }
            },

            "sports_block": {
                "ground": {
                    "booking": "bug"
                }
            }
        },

        "exams": {
            "internal": {
                "marks_entry": {
                    "status": "working"
                }
            },
            "board": {
                "hall_ticket": {
                    "download": {
                        "status": "bug"
                    }
                }
            }
        }
    }

    food_app = {
        "app": "QuickBite",

        "modules": {
            "customer": {
                "home": {
                    "search": {
                        "filter": {
                            "status": "working"
                        }
                    },
                    "offers": "working"
                },

                "cart": {
                    "add_item": {
                        "status": "bug"
                    },
                    "remove_item": {
                        "status": "working"
                    }
                }
            },

            "restaurant": {
                "menu": {
                    "update_price": "bug"
                },
                "orders": {
                    "accept": {
                        "status": "working"
                    },
                    "reject": {
                        "reason": {
                            "status": "bug"
                        }
                    }
                }
            }
        },

        "payments": {
            "upi": {
                "status": "working"
            },
            "card": {
                "otp": {
                    "verify": "bug"
                }
            }
        },

        "support": {
            "chat": "working",
            "call": {
                "connect": {
                    "status": "bug"
                }
            }
        }
    }

    ic(count_bugs(school))
    ic(count_bugs(food_app))

    replacing(school)
    replacing(food_app)

    ic(school)
    ic(food_app)
main()


            
        